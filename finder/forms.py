from django import forms
#from .models import Dweet

class DweetForm(forms.Form):
    body = forms.CharField(label='building_time', required=True)