from django.shortcuts import render
from django.http import HttpResponse


def welcome_view(request):
	print('This line is printed by view function while processing the request')
	x =10/0
	return HttpResponse('<h1>Custom Middleware Demo</h1>')
