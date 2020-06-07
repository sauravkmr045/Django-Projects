from django.shortcuts import render
from app1.forms import Product

# Create your views here.
def addproduct(request):
	form = Product()
	    
	if request.method=='POST':
		name=request.POST,get('name')
		print(name)
		quantity = request.POST.get('quantity')
		print(quantity)
		request.session[name] = quantity
	return render(request,'home.html',{'form': form} )


def display(request):

	
	return render(request,'display.html' )