from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    location = forms.CharField(max_length=100, required=True)