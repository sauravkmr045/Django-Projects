from django.db import models

# Create your models here.
class Movie(models.Model):
	name = models.CharField(max_length= 30)
	year = models.DateField(null = True)
	rating = models.IntegerField()
	hero = models.CharField(max_length=30)
	feedback = models.TextField()

	def __str__(self):
		return self.name + self.hero