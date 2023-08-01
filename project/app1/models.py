from django.db import models

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    DOB=models.DateField()
    phone_number=models.CharField(max_length=12)
    