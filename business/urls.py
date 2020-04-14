from . import views
from django.urls import path 


urlpatterns = [
    path('business/',views.business_home,name='home-page'),
    
]