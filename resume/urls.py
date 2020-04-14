from . import views
from django.urls import path 
urlpatterns = [
    path('resume',views.resume_home,name='home_page'),
    
]