from django.contrib import admin
# from .models import Student, Info, Professor, Faculty,City
from .models import Customer,Product, Order, Manufacturer, Employee

admin.site.register(Manufacturer)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Employee)
