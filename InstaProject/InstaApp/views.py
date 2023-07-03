from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm,RegisterForm,LoginForm
from django.contrib.auth import(
    authenticate,
    login,
    logout
)

def home(request):
    return render(request,'InstaApp/base.html')

def postList(request):
    posts=Post.objects.all()
    return render(request,'InstaApp/postlist.html',{'posts':posts})

@login_required
def viewPost(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    return render(request,'InstaApp/viewpost.html',{'post':post})

@login_required()
def createPost(request):
    if request.method=="POST":
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('InstaApp/postlist.html')
    else:
        form=PostForm()
    return render(request,'InstaApp/postcreate.html',{'form':form})

@login_required
def updatePost(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    if request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('postlist')
    else:
        form=PostForm(instance=post)
    return render(request,'InstaApp/postupdate.html',{'form':form})

@login_required
def deletePost(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    post.delete()
    return redirect('home')



def login_view(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                messages.success(request, f'Login Successfully')
                login(request,user)
                return redirect('home')
            else:
                form.add_error(None,'Invalid Username or password.Try Again')
    else:
        form=LoginForm()
    return render(request,"InstaApp/login.html",{'form':form})

def register_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            password=form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            messages.success(request, f'User Registered Successfully')

            return redirect('login')
    else:
        form=RegisterForm()
    return render(request,'InstaApp/login.html',{'form':form})

@login_required()
def logout_view(request):
    logout(request)
    return redirect('home')




# Create your views here.
