from django_tables2 import tables, TemplateColumn
from .models import Bills

class SimpleTable(tables.Table):
    class Meta:
        orderable = False
        model = Bills
        attrs = {'class': 'fl-table'}
        fields = ['id', 'company_id', 'type_id', 'uuid', 'receiver', 'xml', 'pdf', 'created_at']
    xml = TemplateColumn(template_name='reportes/training_update_column.html',verbose_name='XML')
    pdf = TemplateColumn(template_name='reportes/pdf_logo.html', verbose_name='PDF')