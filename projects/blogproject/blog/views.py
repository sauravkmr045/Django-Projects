from django.shortcuts import render
from  blog.models import Post
from django.views.generic import ListView, DetailView,View, TemplateView,CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger 



def post_list_view(request):

	post_list = Post.objects.all()
	paginator=Paginator(post_list,2)
	page_number=request.GET.get('page')
	try:  
		post_list=paginator.page(page_number)
	except PageNotAnInteger:
		post_list=paginator.page(1)
	except EmptyPage:
		post_list=paginator.page(paginator.num_pages)

	return render(request, 'blog/blog_list.html',{'post_list': post_list})

'''
class post_list_view(ListView):
	model = Post
	template_name ='blog/blog_list.html'
	context_object_name = 'post_list'
	paginate_by = 2
	'''


class post_detail_view(DetailView):
	model = Post
	template_name ='blog/post_detail.html'
	context_object_name = 'post'
	

	
































	# Create your views here.
'''def post_list_view(request):

	post_list = Post.objects.all()
	return render(request, 'blog/blog_list.html',{'post_list': post_list})'''

'''def post_detail_view(request,year,month,day,post):
	post= get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
	return render(request, 'blog/post_detail.html',{'post':post})'''