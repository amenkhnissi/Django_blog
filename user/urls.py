from . import views 
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('register',views.register,name='register'),
    path('signin',views.login,name='login'),
    path('signout',LogoutView.as_view(template_name='user/logout.html'),name='logout'),
    path('myprofile',views.profile,name='myprofile'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)