from django.db import models

# Create your models here.
class Employee(models.Model):

	ename = models.CharField(max_length = 30)
	esal = models.IntegerField()
	eno = models.IntegerField()
	eadd = models.CharField(max_length=30)

	def __str__(self):
		
		return self.ename