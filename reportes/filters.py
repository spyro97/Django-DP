import django_filters
from django_filters import DateFilter, CharFilter

from .models import * 

class BillsFilter(django_filters.FilterSet):
    pk = CharFilter(field_name='pk', lookup_expr='icontains', label='PK')
    created_at = DateFilter(field_name='created_at', lookup_expr='icontains', label = 'FECHA')
    uuid = CharFilter(field_name='uuid', lookup_expr='icontains', label='UUID')
    class Meta:
        model = Bills
        fields = ['pk','uuid', 'receiver', 'created_at']
        exclude = ['xml', 'metadato', 'updated_at', 'type_id', 'company_id']