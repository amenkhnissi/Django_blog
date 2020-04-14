from . import views 
from django.urls import path
from .views import CreatePostView , updatePostView , DeletePostView


urlpatterns = [
    path('',views.blog_home,name='blog-home'),
    path('About/',views.about,name='about-page'),
    path('Contact/',views.contact,name='contact-page'),
    path('Posts/<int:post_id>/',views.postdetail,name='posts-page'),
    path('New_post/',CreatePostView.as_view(),name='new_post'),
    path('Update_post/<slug:pk>/',updatePostView.as_view(),name='update-post'),
    path('Delete_post/<slug:pk>/',DeletePostView.as_view(),name='delete-post'),



]