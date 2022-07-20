from dataclasses import fields
from django.forms import widgets


from .models import UserProfile, Ceremonies, CEREMONY_TYPES
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

class CeremonyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # self.helper.form_method = 'POST'
        # self.helper.form_action = reverse_lazy('profiles:cerlistview')
        # self.helper.add_input(Submit('submit', 'Submit'))


    cer_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}, format={'%d-%m-%Y'}))
    ceremonies = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=CEREMONY_TYPES)#ModelMultipleChoiceField(queryset=CeremonyChoices.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'placeholder': 'Choose Ceremonies'}))

    class Meta:
        model = Ceremonies
        fields = ("user","cer_date", "ceremonies")




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