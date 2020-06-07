class ExecutionFlowMiddleware(object):

	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):

		print('This line is printed at pre Processing of request')
		response = self.get_response(request)

		print('This line is printed Post Processing of request')
		return response

#---------------------------------------------------------------------------------------------------------------------

from django.http import HttpResponse

class AppMaintainanceMiddleware(object):
	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):

		return HttpResponse('<h1>Application is under maintainance <br> Please try after 2 days</h1>')

#--------------------------------------------------------------------------------------------------------------------------

class ErrorMessageMiddleware(object): 
	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):
		response = self.get_response(request)

		return response

	def process_exception(self,reque,exception): # This method will execute when we have any Error in Views.py file
		res1 = '<h1>There is some Technical error please try after sometime</h1><hr>'
		res2 ='<h2>Raised exception is {}</h2><hr>'.format(exception.__class__.__name__)
		res3 = '<h2> Description for the exception is {}'.format(exception)
		return HttpResponse(res1+res2+res3)

















