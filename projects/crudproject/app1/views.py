from django.shortcuts import render, redirect
from app1.forms import EmployeeForm
from app1.models import Employee

# Create your views here.
def display(request):

	data = Employee.objects.all()

	return render(request, 'index.html', {'form': data	})

def create(request):
	form = EmployeeForm()
	if request.method == 'POST':
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	return render(request, 'add.html', {'form': form})

def delete(request,id):
	emp = Employee.objects.get(id = id)
	emp.delete()
	return redirect('/')

def update(request,id):
	emp = Employee.objects.get(id = id)
	if request.method =='POST':
		form = EmployeeForm(request.POST, instance = emp)
		if form.is_valid():
			form.save()
			return redirect('/')

	return render(request,'update.html', {'emp': emp})
