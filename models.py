from django.db import models


# Create your models here.

class passengers(models.Model):
  From=models.CharField(max_length=50)
  To=models.CharField(max_length=50)
  Date=models.DateField()
  no_of_people=models.CharField(max_length=20)

class flit(models.Model):
  name=models.CharField(max_length=50)
  no=models.IntegerField()
  fare=models.IntegerField()
  time=models.CharField(max_length=50)
  image=models.ImageField()

class food(models.Model):
  name=models.CharField(max_length=50)
  no=models.IntegerField()
  food_cost=models.IntegerField()
  image=models.ImageField()
