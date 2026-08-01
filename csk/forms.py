# forms.py
from django import forms

class reviewform(forms.Form):
	allowed_int = [
	(15,15),(16,16),(17,17)
]
	name = forms.CharField()
	age = forms.ChoiceField(choices = allowed_int)
