from django import forms
from .models import Event, Location
from .forms import EventForm

class EventForm(forms.ModelForm):
    location = forms.CharField(max_length=100, required=True)