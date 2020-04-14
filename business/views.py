from django.shortcuts import render
from django.http import HttpResponse 


# Create your views here.
def business_home (request):
    return render (request,'index2.html',{'title':'business_home'})