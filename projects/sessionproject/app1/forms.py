from django import forms

class Product(forms.Form):
	name = forms.CharField()
	quantity = forms.IntegerField()