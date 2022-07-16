from dataclasses import fields
from django.forms import ModelForm,widgets
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile, Ceremonies, CeremonyChoices
from django import forms

class CeremonyForm(forms.ModelForm):
    class Meta:
        model = Ceremonies
        fields = ["cer_date", "ceremonies"]
        labels = {
            'Choose ceremony date': 'Ceremonies Attended',
        }
        widgets = {
            'cer_date': forms.DateInput(
        format=('%d-%m-%Y'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date',
               'label':"Choose a date"
              })
        }
    cer_date = forms.DateInput()
    ceremonies = forms.ModelMultipleChoiceField(queryset=CeremonyChoices.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'placeholder': 'Choose Ceremonies'}))


class UserEditForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput())
    # email = forms.CharField(widget=forms.TextInput())
    class Meta:
        model = UserProfile
        fields = ['email', 'user_name', 'image']
        widgets = {
            'email': widgets.EmailInput(attrs={
                'class':'input is-primary',
                'type': 'email',
                'placeholder':'Email'
            }),
            'user_name': widgets.TextInput(attrs={
                'class': 'input is-primary',
                'type': 'text',
                'placeholder':'Username'
            }),
            'image': widgets.FileInput(attrs={
                'class': 'input-group mb-3',
                'type':'file',
                'placeholder':'Choose an avatar'
            })
        }