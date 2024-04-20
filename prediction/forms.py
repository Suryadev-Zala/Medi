from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib.auth import models
from .models import Images


class ImageForm(forms.Form):
    username=forms.CharField( max_length=100,label="", widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'Username','name':'username'}))
    # name=forms.CharField(max_length=64,label="", widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'Name','name':'name'}))
    image=forms.ImageField(label="", widget=forms.FileInput(attrs={'class':'form-control shadow-none display-3', 'placeholder':'Upload Image','name':'image'}))
    class meta:
        model=User
        fields=('image')
    
# class ChatBotForm(forms.Form):
#     input=forms.TextInput( max_length=100,label="", widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'Username','name':'input'}))
#     # name=forms.CharField(max_length=64,label="", widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'Name','name':'name'}))
#     image=forms.ImageField(label="", widget=forms.FileInput(attrs={'class':'form-control shadow-none display-3', 'placeholder':'Upload Image','name':'image'}))
#     class meta:
#         model=User
#         fields=('input','image')

class CTImageForm(forms.Form):
    username=forms.CharField( max_length=100,label="", widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'Username','name':'username'}))
    # name=forms.CharField(max_length=64,label="", widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'Name','name':'name'}))
    image=forms.ImageField(label="", widget=forms.FileInput(attrs={'class':'form-control shadow-none display-3', 'placeholder':'Upload Image','name':'image'}))
    class meta:
        model=User
        fields=('image')

class XRayImageForm(forms.Form):
    username=forms.CharField( max_length=100,label="", widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'Username','name':'username'}))
    # name=forms.CharField(max_length=64,label="", widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'Name','name':'name'}))
    image=forms.ImageField(label="", widget=forms.FileInput(attrs={'class':'form-control shadow-none display-3', 'placeholder':'Upload Image','name':'image'}))
    class meta:
        model=User
        fields=('image')

class LoginForm(forms.Form):
    username=forms.CharField( max_length=100)
    password=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'Password','name':'password'}))
    class meta:
        model=User
        fields=('username','password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control shadow-none'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].widget.attrs['name'] = 'username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<div class="form-text text-muted "></div>'

class DiabetesForm(forms.Form):
    username=forms.CharField( max_length=100,label="", widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'Username','name':'username'}))
    OGTT=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'OGTT','name':'OGTT'}))
    Blood_Pressure=forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'Blood Pressure','name':'Blood_Pressure'}))
    Skin_Thickness =forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'Skin Thickness','name':'Skin_Thickness'}))
    Insulin=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'Insulin','name':'Insulin'}))
    BMI=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'BMI','name':'BMI'}))
    Age=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'Age','name':'Age'}))
    DiabetesPedigreeFunction=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'DiabetesPedigreeFunction','name':'DiabetesPedigreeFunction'}))

    class meta:
        model=User
        fields=('username','OGTT','Blood_Pressure','Skin_Thickness','BMI','Age','DiabetesPedigreeFunction')
        

class SignUpForm(forms.Form):
    username=forms.CharField( max_length=100)
    email=forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'Email Address','name':'email'}))
    first_name=forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'First Name','name':'first_name'}))
    last_name=forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'Last Name','name':'last_name'}))
    mobile=forms.IntegerField(label="", widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'Mobile Number','name':'mobile'}))
    password=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control shadow-none', 'placeholder':'Password','name':'password'}))

    class meta:
        model=User
        fields=('username','first_name','last_name','email','mobile','password')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control shadow-none'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].widget.attrs['name'] = 'username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<div class="form-text text-muted ">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</div>'

       