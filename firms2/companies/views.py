from django.http import JsonResponse
from .models import Customer,Product, Order, Manufacturer, Employee
from .serializers import CustomerSerializer, OrderSerializer,ProductSerializer, ManufacturerSerializer,EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import CustomerSearchSerializer, ManufacturerSearchSerializer
from rest_framework.status import HTTP_200_OK

from .filters import ManufacturerFilter
from django_filters.rest_framework import DjangoFilterBackend

import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.test import TestCase
from rest_framework.test import APIClient

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from django.http import Http404
# from .models import Manufacturer
# from .views import ManufacturerRevenueView

from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.db.models import Avg

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ManufacturerRevenueSerializer
from .models import Customer
from .serializers import CustomerSerializer


# STUDENNTTTT
@api_view(['GET', 'POST'])
def customer_list(request, format=None):
    if request.method == 'GET':
        #get all students, serialize them, return json
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#shows a detail of a student
@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, id, format=None):
    try:
        customer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# KRAJ SO STUDENT


# INFOOOOOOOO
@api_view(['GET', 'POST'])
def order_list(request, format=None):
    if request.method == 'GET':
        #get all students, serialize them, return json
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#shows a detail of a INFO
@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, id, format=None):
    try:
        order = Order.objects.get(pk=id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# KRAJ SO INFO




#PROFESORIIII
@api_view(['GET', 'POST'])
def product_list(request, format=None):
    if request.method == 'GET':
        #get all students, serialize them, return json
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#shows a detail of a PROFESORI
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id, format=None):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# KRAJ SO PROFESORII




#FAKULLTETII
@api_view(['GET', 'POST'])
def manufacturer_list(request, format=None):
    if request.method == 'GET':
        #get all students, serialize them, return json
        manufacturer = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(manufacturer, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ManufacturerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#shows a detail of a FAKULTETI
@api_view(['GET', 'PUT', 'DELETE'])
def manufacturer_detail(request, id, format=None):
    try:
        manufacturer = Manufacturer.objects.get(pk=id)
    except Manufacturer.DoesNotExist:
        return Manufacturer(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ManufacturerSerializer(manufacturer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ManufacturerSerializer(manufacturer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        manufacturer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# KRAJ SO FAKULTETI





#GRADOVI
@api_view(['GET', 'POST'])
def employee_list(request, format=None):
    if request.method == 'GET':
        #get all students, serialize them, return json
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#shows a detail of a PROFESORI
@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, id, format=None):
    try:
        employee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Employee(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# KRAJ SO GRADOVI


@require_GET
def customer_list(request):
    min_age = request.GET.get('min_age')
    if min_age:
        customers = Customer.objects.filter(years__gte=min_age)
    else:
        customers = Customer.objects.all()
    customer_list = []
    for customer in customers:
        customer_data = {
            'name': customer.name,
            'surname': customer.surname,
            'years': customer.years,
            'email': customer.email,
            'phone': customer.phone
        }
        customer_list.append(customer_data)
    return JsonResponse({'customers': customer_list})

#za customers post so ne rabote voa ako saka da go praam,inace drugo se si rabote u red
# @api_view(['GET', 'POST'])
# def employee_list(request, format=None):
#     if request.method == 'GET':
#         #get all students, serialize them, return json
#         employee = Employee.objects.all()
#         serializer = EmployeeSerializer(employee, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





def order_with_avg_age(request):
    orders = Order.objects.annotate(avg_age=Avg('customer__years')).order_by('-avg_age')
    dto_list = [OrderWithAvgAgeDTO(order.id, order.price, order.delivery_location, order.avg_age) for order in orders]
    response_data = {'orders': [dto.as_dict() for dto in dto_list]}
    return JsonResponse(response_data)


class OrderWithAvgAgeDTO:
    def __init__(self, id, price, delivery_location, avg_age):
        self.id = id
        self.price = price
        self.delivery_location = delivery_location
        self.avg_age = avg_age

    def as_dict(self):
        return {'id': self.id, 'price': self.price, 'delivery_location': self.delivery_location, 'avg_age': self.avg_age}

# class ManufacturerRevenueView(APIView):
#     def get(self, request, manufacturer_id):
#         try:
#             manufacturer = Manufacturer.objects.get(id=manufacturer_id)
#             total_revenue = manufacturer.get_total_revenue()
#             return Response({'total_revenue': total_revenue}, status=status.HTTP_200_OK)
#         except Manufacturer.DoesNotExist:
#             return Response({'error': 'Manufacturer not found'}, status=status.HTTP_404_NOT_FOUND)


#voa e za so id da gi zima
# class ManufacturerRevenueView(APIView):
#     def get(self, request, manufacturer_id):
#         try:
#             manufacturer = Manufacturer.objects.get(id=manufacturer_id)
#             total_revenue = manufacturer.get_total_revenue()
#             response_data = {
#                 'ManufacturerID': manufacturer.id,
#                 'Name': manufacturer.name,
#                 'total_revenue': total_revenue
#             }
#             return Response(response_data, status=status.HTTP_200_OK)
#         except Manufacturer.DoesNotExist:
#             return Response({'error': 'Manufacturer not found'}, status=status.HTTP_404_NOT_FOUND)


class ManufacturerRevenueListView(APIView):
    def get(self, request):
        manufacturers = Manufacturer.objects.all()
        response_data = []
        for manufacturer in manufacturers:
            total_revenue = manufacturer.get_total_revenue()
            manufacturer_data = {
                'id': manufacturer.id,
                'name': manufacturer.name,
                'total_revenue': total_revenue
            }
            response_data.append(manufacturer_data)
        return Response(response_data, status=status.HTTP_200_OK)

class CustomerSearchView(generics.ListAPIView):
    serializer_class = CustomerSearchSerializer
    queryset = Customer.objects.all()

    def get_queryset(self):
        search_query = self.request.query_params.get('q', '')
        queryset = self.queryset.filter(name__icontains=search_query) | self.queryset.filter(email__icontains=search_query)
        return queryset


def get_employee_full_name(request, employee_id):
    # get the employee with the specified id
    employee = Employee.objects.get(pk=employee_id)
    # construct the full name and surname
    full_name = f"{employee.name} {employee.surname}"
    # return a JSON response with the full name
    return JsonResponse({'full_name': full_name})



# def add_products_to_manufacturer(request, manufacturer_id):
#     manufacturer = get_object_or_404(Manufacturer, pk=manufacturer_id)

#     if request.method == 'POST':
#         product_ids = request.POST.getlist('product_ids')
#         products = Product.objects.filter(pk__in=product_ids)
#         for product in products:
#             product.manufacturer = manufacturer
#             product.save()

#         return JsonResponse({'status': 'success'})


@csrf_exempt
def add_products_to_manufacturer(request, manufacturer_id):
    if request.method == 'POST':
        try:
            manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
            data = json.loads(request.body)
            products = data['products']
            for product_id in products:
                product = Product.objects.get(pk=product_id)
                product.manufacturer = manufacturer
                product.save()
            response = {
                'status': 'success',
                'message': f'Added products to manufacturer {manufacturer_id}'
            }
            return JsonResponse(response)
        except Manufacturer.DoesNotExist:
            response = {
                'status': 'error',
                'message': f'Manufacturer with ID {manufacturer_id} does not exist'
            }
            return JsonResponse(response, status=404)
        except Exception as e:
            response = {
                'status': 'error',
                'message': str(e)
            }
            return JsonResponse(response, status=400)



#manufacturer filter

class ManufacturerSearchView(generics.ListAPIView):
    serializer_class = ManufacturerSearchSerializer
    queryset = Manufacturer.objects.all()

    def get_queryset(self):
        search_query = self.request.query_params.get('q', '')
        queryset = self.queryset.filter(name__icontains=search_query)
        return queryset