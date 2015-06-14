from django import forms
from .models import Subscription

class EmailForm(forms.Form):
	email = forms.EmailField()
