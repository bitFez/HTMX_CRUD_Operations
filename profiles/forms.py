from django.forms import ModelForm,widgets
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile
from django import forms

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