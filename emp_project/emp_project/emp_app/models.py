from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    emp_id=models.IntegerField(primary_key=True)
    email=models.EmailField(max_length=150,unique=True)
    phone=models.IntegerField()
    gender=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    emp_type = models.CharField(max_length=50)
    salary=models.FloatField(max_length=55)
