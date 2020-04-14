from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(default=None,null=True,max_length=100)
    facebook = models.CharField(default='https://www.facebook.com/',null=True,max_length=100)
    twitter = models.CharField(default=None,null=True,max_length=100)
    instagram = models.CharField(default=None,null=True,max_length=100)
    linkedin = models.CharField(default=None,null=True,max_length=100)


    def __str__(self):
        return '{} profile'.format(self.user.username)
   

def create_profile(sender,**kwarg):
    if kwarg['created']:
       Profile.objects.create(user=kwarg['instance'])

post_save.connect(create_profile,sender=User)
