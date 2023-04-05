from django.db import models
import django.db.models.deletion
from decimal import Decimal


# class (models.Model):
#     username = models.CharField(max_length=200)

#     def __str__(self):
#         return self.username
    
class Customer(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    years = models.IntegerField()
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    

    def __str__(self): #str(self.field_name)
        return self.name + ', ' + self.surname + ', ' + str(self.years) + ', ' + self.email + ', ' + self.phone



        
class Order(models.Model):
    price = models.CharField(max_length=200)
    delivery_location = models.CharField(max_length=200)
    customer = models.ManyToManyField(Customer, blank=True, null=True)
    product = models.ManyToManyField("Product", blank=True, null=True)

    def __str__(self):
        customer_names = ', '.join(str(s) for s in self.customer.all()) if self.customer.exists() else "None"
        product_names = ', '.join(str(p) for p in self.product.all()) if self.product.exists() else "None"
        return f"{self.price}, {self.delivery_location}, customers: {customer_names}, products: {product_names}"
   








    # @staticmethod # to test it: longer_songs = Song.objects.filter(duration__gte=300)
    # def filter_by_duration(min_duration=None, max_duration=None): # only entities higher than a given value, but we can do higher-lower too
    #     """
    #     Filters songs based on the provided min_duration and max_duration values.

    #     :param min_duration: The minimum duration in seconds. If None, the filter will not include a minimum duration.
    #     :param max_duration: The maximum duration in seconds. If None, the filter will not include a maximum duration.
    #     :return: A QuerySet containing the filtered songs.
    #     """
    #     queryset = Song.objects.all()

    #     if min_duration is not None:
    #         queryset = queryset.filter(duration__gte=min_duration)

    #     if max_duration is not None:
    #         queryset = queryset.filter(duration__lte=max_duration)

    #     return queryset

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    company = models.CharField(max_length=10)
    sector = models.CharField(max_length=20)
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ', ' + self.description+ ', ' + self.price + ', ' + self.company + ', ' +self.sector + ', ' + str(self.manufacturer)
    


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=254)
    owner = models.CharField(max_length=20)
    field = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
   

    def __str__(self):
        return self.name + ', ' + self.country+ ', ' + self.owner + ', ' + self.field + ', ' +self.size
    def get_products(self):
        return Product.objects.filter(manufacturer=self)
    def get_manufacturer(self):
        return Manufacturer.objects.filter(employee=self)

    def get_total_revenue(self):
        products = self.product_set.all()
        if not products:
            return 0
        total_revenue = sum(Decimal(product.price) for product in products)
        return total_revenue


class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=20)
    manufacturer = models.OneToOneField(Manufacturer, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name + ', ' + self.surname + ' (' + str(self.manufacturer) + ')'

    
    
