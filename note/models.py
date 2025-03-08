from django.db import models
from datetime import datetime

# Create your models here.
class notes(models.Model):
    check_username = models.CharField(max_length=10000, default=None)
    content = models.CharField(max_length=100000,default = None)
    created_at = models.DateTimeField(default=datetime.now)
