from django import forms
from .models import Breed, HumanProfile, DogProfile

class BreedForm(forms.ModelForm):
    new_breed = forms.CharField(required=False, label='Or add a new breed')

    class Meta:
        model = Breed
        fields = ['breed']

    def clean(self):
        cleaned_data = super().clean()
        breed = cleaned_data.get('breed')
        new_breed = cleaned_data.get('new_breed')

        if not breed and not new_breed:
            raise forms.ValidationError('You must either select an existing breed or enter a new breed.')

        if breed and new_breed:
            raise forms.ValidationError('You cannot select an existing breed and enter a new breed at the same time.')

        return cleaned_data


class DogProfileForm(forms.ModelForm):
    class Meta:
        model = DogProfile
        fields = ['name', 'breed', 'age', 'bitten', 'rough_play', 'vaccinated']

class HumanProfileForm(forms.ModelForm):
    class Meta:
        model = HumanProfile
        fields = ['name', 'dogs']
    dogs = forms.ModelMultipleChoiceField(queryset=DogProfile.objects.all(), widget=forms.CheckboxSelectMultiple)