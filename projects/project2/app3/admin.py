from django.contrib import admin

# Register your models here.
from app3.models import Class

class ClassAdmin(admin.ModelAdmin):
	list_display = ['name','rollno','cl','branch']

admin.site.register(Class, ClassAdmin)
