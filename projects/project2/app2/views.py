from django.shortcuts import render
from app2 import forms

# Create your views here.

def moviedetails(request):

	form = forms.MovieForm(request.POST)
	if request.method == 'POST':
		if form.is_valid:
			form.save(commit = True)
	return render(request, 'movie.html', {'form':form})
