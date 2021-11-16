from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin import widgets 

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
            super(ConferenceForm, self).__init__(*args, **kwargs)

class TalkForm(ModelForm):
    class Meta:
        model = Talk
        exclude = ['host']
        fields = ['title', 'description', 'conference', 'speakers', 'participants', 'date_time', 'duration']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Talk title'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Talk description'}),
            'conference':forms.Select(choices=Conference.objects.all().values_list('title', 'title'), attrs={'class':'form-control'}),
            # 'date_time':forms.DateTimeInput(attrs={'class':'form-control'}),
            'date_time':forms.DateTimeInput(),
            'speakers':forms.SelectMultiple(choices=User.objects.all(), attrs={'class':'form-control'}),
            'participants':forms.SelectMultiple(choices=User.objects.all(), attrs={'class':'form-control'}),
            'duration':forms.TextInput(attrs={'class':'form-control',  'placeholder':'Talk duration'}),
        }

        def __init__(self, *args, **kwargs):
            super(TalkForm, self).__init__(*args, **kwargs)

class AddSpeakerForm(ModelForm):
    class Meta:
        model = Talk
        fields = ['speakers']

        widgets={
            'speakers':forms.SelectMultiple(choices=User.objects.all(), attrs={'class':'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super(AddSpeakerForm, self).__init__(*args, **kwargs)

class RemoveSpeakerForm(ModelForm):
    class Meta:
        model = Talk
        fields = ['speakers']

        widgets={
            'speakers':forms.SelectMultiple(choices=Talk.objects.all().values_list('speakers', 'speakers'), attrs={'class':'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super(RemoveSpeakerForm, self).__init__(*args, **kwargs)

        
class AddParticipantForm(ModelForm):
    class Meta:
        model = Talk
        fields = ['participants']

        widgets={
            'participants':forms.SelectMultiple(choices=User.objects.all(), attrs={'class':'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super(AddParticipantForm, self).__init__(*args, **kwargs)

class RemoveParticipantForm(ModelForm):
    class Meta:
        model = Talk
        fields = ['participants']

        widgets={
            'participants':forms.SelectMultiple(choices=Talk.objects.all().values_list('participants', 'participants'), attrs={'class':'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super(RemoveParticipantsForm, self).__init__(*args, **kwargs)

