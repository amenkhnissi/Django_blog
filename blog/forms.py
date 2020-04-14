from django import forms
from .models import Comment 
from django.contrib.auth.models import User 


class newcomment (forms.ModelForm):
    class Meta:
        model = Comment 
        fields =('username','email','body')
        

    
    
    


