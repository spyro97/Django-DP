from django_tables2 import tables, TemplateColumn
from .models import Bills

class SimpleTable(tables.Table):
    class Meta:
        model = Bills
        attrs = {'class': 'table table-sm'}
        fields = ['pk', 'company_id', 'type_id', 'uuid', 'receiver', 'created_at', 'xml',]
    xml = TemplateColumn(template_name='reportes/training_update_column.html')