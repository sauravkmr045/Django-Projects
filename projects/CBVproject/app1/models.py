from django.db import models
from django.urls import reverse
# Create your models here.
class Book(models.Model):
	name = models.CharField(max_length =250)
	author = models.CharField(max_length=50)
	pages = models.IntegerField()
	price = models.FloatField()

	def get_absolute_url(self,**kwargs):
		return reverse('detail',kwargs ={'pk':self.pk})