
from django import forms

class message(forms.Form):
    message = forms.CharField(label='message', max_length=50000)