from django.shortcuts import render
from django.views.generic import ListView, DetailView,View, TemplateView,CreateView, UpdateView, DeleteView
from app1.models import Book
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.
#LIST VIEW APPLICATION

class booklist(ListView):
	model = Book
	template_name ='book_list.html'
	context_object_name = 'book_list'

	#default tmeplate Name :  modelname_list   in smaller case only
	#default contex Name : modelname_list     in smaller case only

# DETAIL VIEW APPLICATION

class bookdetail(DetailView):
	model = Book
	template_name ='book_detail.html'
	context_object_name = 'book'

	#default tmeplate Name :  modelname_detial     in smaller case
	#default contex Name : modelname      in smallcase

# SIMPLE VIEW APPLICATION

class simpleview(View):

	def get(self,request):

		return HttpResponse('<h1>Hi This is coming from simple class based view</h1>')


class templateview(TemplateView):
	template_name = 'templateview.html'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['name'] = 'Saurav Kumar'
		context['prof'] = 'Software Developer'
		return context

#CREATE VIEW APPLICATION
class createview(CreateView):
	model = Book
	fields =['name','author', 'pages','price']
	template_name ='book_form.html'



class updateview(UpdateView):
	model = Book
	template_name ='book_form.html'
	fields =['name','author', 'pages','price']


class deleteview(DeleteView):
	model= Book
	success_url = reverse_lazy('home')
	template_name = 'book_confirm_delete.html'













