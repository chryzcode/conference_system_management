from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

#custom signup/ register form
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


# add and edit conference form
class ConferenceForm(ModelForm):
    class Meta:
        model = Conference
        exclude = ['host']
        fields = ['title', 'description', 'start_date', 'end_date']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Conference title'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Conference description'}),
            'start_date':forms.TextInput(attrs={'class':'form-control',  'placeholder':'The first day of the conference'}),
            'end_date':forms.TextInput(attrs={'class':'form-control',  'placeholder':'The last day of the conference'}),
        }
        def __init__(self, *args, **kwargs):
            super(UserWalletForm, self).__init__(*args, **kwargs)



