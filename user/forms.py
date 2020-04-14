from django import forms
from django.contrib.auth.models import User 
from .models import Profile 


class registerform (forms.ModelForm):
    username = forms.CharField(label='Username',max_length=30)
    email = forms.EmailField(label='Your Email',)
    first_name = forms.CharField(label='Firstname')
    last_name = forms.CharField(label='Lastname')
    password1 = forms.CharField(label='Enter your Password',widget=forms.PasswordInput(),min_length=8)
    password2 = forms.CharField(label='Re-enter your Password',widget=forms.PasswordInput(),min_length=8)
       

    class Meta:
        model = User 
        fields =('username','email','first_name','last_name','password1','password2')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd ['password2']:
             raise forms.ValidationError('Password didnt match')
        return cd ['password2']

    def clean_username(self):
        cd = self.cleaned_data 
        if User.objects.filter(username=cd['username']).exists():
         raise forms.ValidationError('Username already exist')
        return cd['username']

    def clean_email(self):
        cd = self.cleaned_data 
        if User.objects.filter(email=cd['email']).exists():
         raise forms.ValidationError('Email already exist')
        return cd['email']    


class loginForm (forms.ModelForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password',widget=forms.PasswordInput())
    class Meta:
        model = User 
        fields =('username','password')


class UserUpdateForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')
        


class ProfileUpdateForm (forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ('about','image',)



class SocialForm (forms.ModelForm):
    facebook = forms.CharField(label='Facebook')
    twitter = forms.CharField(label='twitter')
    instagram = forms.CharField(label='instagram')
    linkedin = forms.CharField(label='linkedin')
    class Meta:
        model = Profile 
        fields = ('facebook','twitter','instagram','linkedin')



        
        
