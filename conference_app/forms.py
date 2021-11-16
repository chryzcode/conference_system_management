from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    full_name = forms.CharField(max_length = 200)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('full_name', 'username', 'email','password1', 'password2')

    def __init__ (self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)


        self.fields['full_name'].widget.attrs['class']= 'form-control'
        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['email'].widget.attrs['class']= 'form-control'
        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['class']= 'form-control'

class ConferenceForm(ModelForm):
    class Meta:
        model = Conference
        exclude = ['host']
        fields = ['title', 'description', 'start_date', 'end_date']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Conference title'}),
            'package_price':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'$ Package Price'}),
            'package_description':forms.Textarea(attrs={'class':'form-control',  'placeholder':'Package description...'}),
        }



