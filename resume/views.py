from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def resume_home (request):
    return render (request,'index.html',{'title':'home_page'})