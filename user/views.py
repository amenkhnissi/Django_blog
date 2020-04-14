from django.shortcuts import render,redirect
from .forms import registerform , loginForm ,  UserUpdateForm , ProfileUpdateForm ,SocialForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as auth_login
from blog.models import post
from django.core.paginator import Paginator , PageNotAnInteger ,EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin




def register (request):
    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
             new_user = form.save(commit=False)
             new_user.set_password(form.cleaned_data['password1'])
             new_user.save()
             messages.success(request,f'Congratulation {new_user} You’ve successfully registered')
             return  redirect('login')

    else:
         form = registerform()


         
    return render (request,'user/register.html',{
        'title' : 'RegisterForm',
        'form'  : form,

    })

def login (request):
    if request.method == 'POST':
          form = loginForm()
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(request, username=username, password=password)
          if  user is not None:
                auth_login(request, user)
                return  redirect('myprofile')
          else:
              messages.warning(request, 'Password Or Username is incorrect. ')    
    else:
        form = loginForm()  
    return render (request,'user/login.html',{
        'form' : form, 
    })


def profile (request):
    
    posts   = post.objects.filter(author=request.user)
    n_posts = post.objects.filter(author=request.user)


    paginator = Paginator(posts, 4)
    page      = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
            posts = paginator.page(1)
    except EmptyPage:
            posts = paginator.page(paginator.num_page)    


    if request.method == 'POST':

        s_form = SocialForm(request.POST, instance=request.user.profile)
        if s_form.is_valid():
            s_form.save()
            messages.success(request,f' Profile successfully updated')
            return  redirect('myprofile')

    else:
        s_form = SocialForm(instance=request.user.profile)


    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request,f' Profile successfully updated')
            return  redirect('myprofile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        


    if request.method == 'POST':

        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        
        if p_form.is_valid():
            p_form.save()
            messages.success(request,f' Profile successfully updated')
            return  redirect('myprofile')

    else:

        p_form = ProfileUpdateForm(instance=request.user.profile)    

    
    

    return render (request,'user/profile.html',{
        'title' : 'My Profile',
        'u_form' : u_form,
        'p_form' : p_form,
        's_form' : s_form,
        'posts'  : posts,
        'page'   : page,
        'n_posts': n_posts,
        
       
        
    })
