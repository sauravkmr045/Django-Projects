from django.db import models

# Create your models here.

class Class(models.Model):
	rollno = models.IntegerField()
	cl = models.IntegerField()
	name = models.CharField(max_length=30)
	branch = models.CharField(max_length =30)

