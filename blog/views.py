from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from .models import post , Comment , Category
from django.utils import timezone
from .forms import newcomment 
from django.core.paginator import PageNotAnInteger , Paginator , EmptyPage
from django.views.generic import CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import  LoginRequiredMixin



# Create your views here.
def blog_home (request):
    posts = post.objects.all()
    paginator = Paginator(posts, 3)
    page      = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
            posts = paginator.page(1)
    except EmptyPage:
            posts = paginator.page(paginator.num_page)   

    context= {
        'posts':posts,
    }

    posts = post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render (request,'index3.html',context)
    
    

def about (request):
    return render (request,'about.html',)  

def contact (request):
    return render (request,'contact.html',)  


def postdetail (request,post_id):
    postc = get_object_or_404(post,pk=post_id)
    commentss = postc.comments.all().filter(active=True)
    category = post.objects.all().filter(category=postc.category)
    
    n_comment = None 

    if request.method == 'POST':
        new_comment = newcomment(data=request.POST)

        if new_comment.is_valid():
            n_comment = new_comment.save(commit=False)
            n_comment.postc = postc 
            n_comment.save()
            new_comment = newcomment()
    else:
        new_comment = newcomment(instance= request.user )        

    return render (request,'post.html',{

        'posts':postc,
        'commentss':commentss,
        'new_comment': new_comment ,
        'category' : category,
    }
)  

class CreatePostView(LoginRequiredMixin, CreateView):
    model = post
    fields = ['title','subtitle','text','image','category']   
    template_name = 'new_post.html'
     

    def form_valid(self,form):
         form.instance.author = self.request.user
         return super().form_valid(form)

class updatePostView(LoginRequiredMixin, UpdateView):
    model = post
    fields = ['title','subtitle','text','image','category']   
    template_name = 'new_post.html'
   
     

    def form_valid(self,form):
         form.instance.author = self.request.user
         return super().form_valid(form)

class DeletePostView(LoginRequiredMixin, DeleteView):
       model = post 
       success_url = '/'
