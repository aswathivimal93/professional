from django.db import models

# Create your models here.
from django.db.models import Model


class services(models.Model):
        name=models.CharField(max_length=250)
        des=models.TextField()
        image=models.ImageField(upload_to='service_pics')

        def __str__(self):
                return self.name
class members(models.Model):
        name=models.CharField(max_length=250)
        desig=models.CharField(max_length=250)
        image=models.ImageField(upload_to='members_pics')

        def __str__(self):
                return self.name
