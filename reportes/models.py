from django.db import models
from django.conf import settings
from django.utils import timezone

class Bills(models.Model):
    company_id = models.IntegerField(verbose_name='Id compañia')
    type_id = models.IntegerField()
    uuid = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    xml = models.TextField()
    metadato = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.receiver
