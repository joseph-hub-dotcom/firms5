"""professors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from companies import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CustomerSearchView, ManufacturerSearchView
from .views import ManufacturerRevenueListView
from .views import get_employee_full_name
# from .views import add_products_to_manufacturer
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Notes API",
        default_version='v1',
        description="Note API built by CodevoWeb",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', views.customer_list),
    path('customers/<int:id>/', views.customer_detail),
    path('customers/search/', CustomerSearchView.as_view()),
    path('orders/', views.order_list),
    path('orders/<int:id>/', views.order_detail),
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),
    path('manufacturers/', views.manufacturer_list),
    path('manufacturers/<int:id>/', views.manufacturer_detail),
    path('manufacturers/<int:manufacturer_id>/add-products/', views.add_products_to_manufacturer, name='add_products_to_manufacturer'),
    path('manufacturers/revenue/', ManufacturerRevenueListView.as_view()),
    path('manufacturers/search/', ManufacturerSearchView.as_view()),
    path('employees/', views.employee_list),
    path('employees/<int:id>/', views.employee_detail),
    path('employee/<int:employee_id>/full_name/', get_employee_full_name),
    path('order-with-avg-age/', views.order_with_avg_age, name='order-with-avg-age'),
    re_path(r'^swagger(?P<file_format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'), re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
