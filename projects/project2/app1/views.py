from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Employee	
from app1 import forms

# Create your views here.
def home(request):

	return render(request, 'home.txt')

def empview(request):

	emplist= Employee.objects.order_by('eadd')

	my_dict =  {"emplist" : emplist}

	return render(request, 'data.html', context = my_dict)

def register(request):
	form = forms.register()
	if request.method== 'GET':
		return render(request, 'register.html', {'form':form})
		
	if request.method == 'POST':
		form = form.register(request.POST)
		if form.is_valid:
			print('Here is the Feedback form info')
			print('Name', form.cleaned_data['name'])
			print('Roll No', form.cleaned_data['rollno'])
			print('classs', form.cleaned_data['classs'])
			print('Section', form.cleaned_data['section'])
			print('Feedback', form.cleaned_data['feedback'])
			return empview(request)

