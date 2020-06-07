from django.db import models

# Create your models here.

class Employee(models.Model):
	ename= models.CharField(max_length =40)
	eno = models.IntegerField()
	eadd = models.CharField(max_length =40)
	esal = models.FloatField()
