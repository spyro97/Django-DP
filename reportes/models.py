from django.db import models
from django.conf import settings
from django.utils import timezone

class Bills(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    company_id = models.IntegerField(verbose_name='COMPAÑIA')
    type_id = models.IntegerField(verbose_name='TIPO ID')
    uuid = models.CharField(max_length=255, verbose_name='UUID')
    receiver = models.CharField(max_length=255, verbose_name='RECEPTOR')
    xml = models.TextField(verbose_name='XML')
    metadato = models.TextField(verbose_name='METADATO')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='FECHA CREADO')
    updated_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.receiver
