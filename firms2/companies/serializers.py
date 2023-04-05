from rest_framework import serializers
from .models import Customer,Product, Order, Manufacturer, Employee
from django.core.exceptions import ValidationError
from django.db.models import Q

# STUDENT SERIALIZER
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'surname', 'years', 'email', 'phone']

        # def validate_email(self, value):
        #     if value.endswith('@example.com'):
        #         raise serializers.ValidationError({'email': 'Email address cannot end with @example.com'})
        #     return value


# PROFESSOR SERIALIZER
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'company', 'sector','manufacturer']

    def validate_price(self, value):
        """
        Validates that the price of the product is a valid number.
        """
        try:
            price = float(value)
            if price <= 0:
                raise ValidationError("Price must be a positive number.")
        except ValueError:
            raise ValidationError("Price must be a valid number.")
        return value

        
# INFO SERIALIZER
class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(many=True, read_only=True)
    product = ProductSerializer(many=True, read_only=True)
    class Meta:
        model =Order
        fields = ['id', 'price', 'delivery_location', 'customer', 'product']

# FACULTY SERIALIZER
class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'country', 'owner', 'field', 'size']


# CITY SERIALIZER
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'surname', 'manufacturer']

    def validate_name(self, value):
        """
        Validates that the name of the employee contains only alphabetic characters.
        """
        if not value.isalpha():
            raise ValidationError("Name must contain only alphabetic characters.")
        return value






# FACULTY SERIALIZER
class ManufacturerSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    # employee = serializers.SerializerMethodField()

    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'country', 'owner', 'field', 'size', 'products','employee']
        depth = 1

    def get_products(self, obj):
        products = obj.get_products()
        return ProductSerializer(products, many=True).data
    def get_manufacturer(self, obj):
        manufacturer = obj.get_manufacturer()
        return ManufacturerSerializer(manufacturer, many=True).data

    def validate_owner(self, value):
            """
            Validates that the owner of the manufacturer is not a numeric string.
            """
            try:
                int_value = int(value)
            except ValueError:
                return value
            else:
                if isinstance(int_value, int):
                    raise ValidationError("Owner must be a valid string.")
            return value



class CustomerSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'surname', 'years', 'email', 'phone')


class ManufacturerRevenueSerializer(serializers.Serializer):
    total_revenue = serializers.FloatField()


class ManufacturerSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'country', 'owner', 'field', 'size')