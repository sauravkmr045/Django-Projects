from django import forms
from django.core import validators


def starts_with_d(val):
	if val[0] != 'd':
		raise froms.ValidationError('The name should starts_with_d ')

class register(forms.Form):
	name = forms.CharField(validators= [starts_with_d])
	rollno = forms.IntegerField()
	classs = forms.CharField()
	section = forms.CharField()
	feedback = forms.CharField(widget = forms.Textarea, validators=[validators.MaxLengthValidator(40), 
								validators.MinLengthValidator(10)])
	password = forms.CharField(widget = forms.PasswordInput)
	rpassword = forms.CharField(label = 'password again' ,widget = forms.PasswordInput)
	bot_handler = forms.CharField(required = False, widget = forms.HiddenInput)


	'''def clean_name(self):
		inputname = self.cleaned_data['name']
		print('Validating name')
		if len(inputname)<=4:
			raise forms.ValidationError('The length of the should be greater than 4')
		return inputname 

	def clean_rollno(self):
		inputrollno = self.cleaned_data['rollno']
		print('Validating Name')
		if inputrollno < 0 or inputrollno >100 :
			raise forms.ValidationError("The roll no can be negative and can't be greater than 100 ")
		return inputrollno	'''

'''
	def clean(self):
		cleaned_data = super.clean()
		inputname = cleaned_data['name']
		if len(inputname) < 4:
			raise forms.ValidationError('The length of the name should be altest 4 char long')
		rollno = cleaned_data['rollno']
		if rollno < 0:
			raise forms.ValidationError("roll number can't be negative")


		
		bot_hadler = cleaned_data['bot_handler']
		if len(bot_handler)> 0:
			raise forms.ValidationError('You are caught my bot')
			
			

'''

