# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase

# from companies.models import Customer
# from companies.serializers import CustomerSearchSerializer


# class CustomerSearchViewTestCase(APITestCase):
#     def setUp(self):
#         # Create some customer objects for testing
#         self.customer1 = Customer.objects.create(name='Josif',surname='doe',years='65', email='johndoe@example.com',phone='233')
#         self.customer2 = Customer.objects.create(name='Martin',surname='Doea',years='123', email='johndoe@example.com',phone='213')
#         self.customer3 = Customer.objects.create(name='Trajce',surname='Doeq',years='225', email='johadoe@non-existent.com',phone='133')

    # def test_customer_search(self):
    #     # Test searching for customers with 'doe' in their name
    #     url = reverse('customer_search')
    #     response = self.client.get(url, {'q': 'Trajc'})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     # expected_data = CustomerSearchSerializer([self.customer1, self.customer2], many=True).data
    #     expected_data = CustomerSearchSerializer([self.customer3], many=True).data
    #     self.assertEqual(response.data, expected_data)

    #     # Test searching for customers with 'example.com' in their email
    #     response = self.client.get(url, {'q': 'example.com'})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     expected_data = CustomerSearchSerializer([self.customer1, self.customer2, self.customer3], many=True).data
    #     self.assertEqual(response.data, expected_data)

    #     # Test searching for customers with 'non-existent' in their name or email
    #     response = self.client.get(url, {'q': 'non-existent'})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, [])

        # response = self.client.get(url, {'q': 'zzzzz'})
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data, [])

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from decimal import Decimal
from companies.models import Manufacturer, Product, Customer
from companies.serializers import ManufacturerRevenueSerializer


# class ManufacturerRevenueViewTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.manufacturer = Manufacturer.objects.create(
#             name='Manufacturer1',
#             country='Country1',
#             owner='Owner1',
#             field='Field1',
#             size='Size1'
#         )

#     def test_get_manufacturer_revenue(self):
#         product1 = Product.objects.create(
#             name='Product1',
#             price=10.5,
#             manufacturer=self.manufacturer
#         )
#         product2 = Product.objects.create(
#             name='Product2',
#             price=20.75,
#             manufacturer=self.manufacturer
#         )
#         expected_revenue = Decimal('31.25')
#         response = self.client.get(f'/manufacturers/{self.manufacturer.id}/revenue/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, {'total_revenue': (expected_revenue)})


class CustomerSearchViewTestCase(APITestCase):
    def setUp(self):
        self.customer1 = Customer.objects.create(name='John', surname='Doe', years=30, email='john@example.com', phone='555-1234')
        self.customer2 = Customer.objects.create(name='Jane', surname='Doe', years=28, email='jane@example.com', phone='555-5678')
        self.customer3 = Customer.objects.create(name='Bob', surname='Smith', years=35, email='bob@example.com', phone='555-9012')

    def test_search_customer_by_name(self):
        search_query = 'John'
        response = self.client.get('/customers/search/', {'q': search_query})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.customer1.name)

    def test_search_customer_by_email(self):
        search_query = 'jane@example.com'
        response = self.client.get('/customers/search/', {'q': search_query})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['email'], self.customer2.email)

    def test_search_customer_no_results(self):
        search_query = 'nonexistingcustomer@example.com'
        response = self.client.get('/customers/search/', {'q': search_query})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)