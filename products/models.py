from django.db import models# from django.db package, we import models module

# Create your models here.


class Products(models.Model):#we creare a prouduct model class based on Model class in the models module
    name=models.CharField(max_length=50)
    price=models.FloatField()
    stock=models.IntegerField()
    description=models.CharField(max_length=150)
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    discount=models.FloatField()

class Users(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=40)
    email=models.CharField(max_length=70)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=15)
    PhoneNumber=models.IntegerField (default=999999)