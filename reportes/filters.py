import django_filters
from django_filters import DateFilter, CharFilter

from .models import * 

class BillsFilter(django_filters.FilterSet):
    pk = CharFilter(field_name='pk', lookup_expr='icontains', label='Pk')
    created_at = DateFilter(field_name='created_at', lookup_expr='gte', label = 'Fecha')
    uuid = CharFilter(field_name='uuid', lookup_expr='icontains', label='uuid')
    class Meta:
        model = Bills
        fields = '__all__'
        exclude = ['xml', 'metadato', 'updated_at', 'type_id', 'company_id']