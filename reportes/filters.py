import django_filters
from django_filters import DateFilter, CharFilter

from .models import * 

class BillsFilter(django_filters.FilterSet):
    uuid = CharFilter(field_name='uuid', lookup_expr='icontains')
    pk = CharFilter(field_name='pk', lookup_expr='icontains')
    class Meta:
        model = Bills
        fields = '__all__'
        exclude = ['xml', 'metadato', 'updated_at', 'type_id', 'company_id']