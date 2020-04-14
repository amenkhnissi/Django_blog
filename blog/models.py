from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

class Category (models.Model):
    title =models.CharField(max_length=100) 
    slug = models.SlugField(max_length=40)
      
    def __str__(self):
        return self.title




class post (models.Model):

   title =models.CharField(max_length=100)
   image = models.ImageField(default='default_1.jpg',upload_to='post_pics')
   text  =models.TextField()
   subtitle=models.CharField(max_length=100,default=None)
   author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
   created_date =models.DateTimeField(default=timezone.now)
   published_date =models.DateTimeField(blank=True, null=True)
   category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='Categorys',blank=True, null=True)

   def __str__(self):
        return self.title


   def get_absolute_url(self):
        return reverse('posts-page', args=[self.pk])     

   class Meta :
      ordering = ('-created_date', )   



class Comment (models.Model):
    username = models.CharField(max_length=50, verbose_name='Name')
    email = models.EmailField(verbose_name='Email address')
    body = models.TextField(verbose_name='comment')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    postc = models.ForeignKey(post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return 'comment {} on {}.'.format(self.username, self.postc)

    class Meta:
        ordering = ('-comment_date',)

 

   
    
     

    
    

   
