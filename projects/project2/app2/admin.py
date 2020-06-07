from django.contrib import admin
from app2.models import Movie
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
	list_display = ['name','hero','rating','year','feedback']


admin.site.register(Movie, MovieAdmin)
