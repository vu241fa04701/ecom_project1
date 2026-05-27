from django.db import models

# Create your models here.
"""
create a model Book Model
give the attributes like id,book_title,book_des,book_type,book_author,book_price,book_quantity
"""
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=200)
    book_des = models.TextField(max_length=200)
    book_type = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)
    book_price = models.CharField(max_length=200)
    book_quantity = models.IntegerField()
class UserModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
