from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    salary = models.IntegerField()
    gender = models.CharField(max_length=20)

