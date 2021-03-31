from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class employee(models.Model):
    empname=models.CharField(max_length=50,default=1)
    mobileno = models.CharField(max_length=50, default=1)

    def __str__(self):
        return self.empname
