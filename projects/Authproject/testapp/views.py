from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm	
from django.http import HttpResponseRedirect
def home(request):
	return render(request, 'home.html')

@login_required
def java(request):
	return render(request, 'java.html')


def thanks(request):
	return render(request, 'thaks.html')

# Create your views here.

def signup(request):
	form = SignUpForm()
	if request.method == 'POST':
		#if form.is_valid():
		#	form.save()
		form  = SignUpForm(request.POST)
		user = form.save()
		user.set_password(user.password)
		user.save()
		form.save()
		return HttpResponseRedirect('/accounts/login')
	return render(request, 'signup.html',{'form': form})


	pass