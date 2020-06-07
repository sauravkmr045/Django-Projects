from django.shortcuts import render
from app3.models import Class
# Create your views here.

def myhome(request):
	data = Class.objects.all()
	return render(request, 'myhome.html',{'data':data})
