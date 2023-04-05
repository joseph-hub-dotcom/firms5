import django_filters
from .models import Manufacturer

class ManufacturerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Manufacturer
        fields = ['name']
