from django.shortcuts import render

# Create your views here.
def cookie_count(request):
	count = int(request.COOKIES.get('count',0))
	newcount = count + 1
	response =  render(request,'cookie.html', {'count': newcount})
	response.set_cookie('count', newcount, max_age =180)
	return response

	# Here COOKIE is the dictionary which stores the no of times we visited the page


def session_count(request):
	count = request.session.get('count',0)
	newcount = count + 1
	request.session['count'] = newcount
	print(request.session.get_expiry_date())
	print(request.session.get_expiry_age())
	#request.session.set_expiry(500)

	return render(request,'cookie.html', {'count': newcount})
