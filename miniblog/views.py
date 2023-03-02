from django.shortcuts import render, HttpResponseRedirect
from . forms import SignUpForm, SignInForm, AddForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . models import BlogPost
from django.contrib.auth.models import Group
# Create your views here.

def home(request):
    posts = BlogPost.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'miniblog/home.html', context)

def about(request):
    return render(request, 'miniblog/about.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts = BlogPost.objects.all()
        ip = request.session.get('ip', 0)
        context = {
            'posts': posts,
            'ip': ip,
        }
        return render(request, 'miniblog/dashboard.html', context)
    else:
        return HttpResponseRedirect('/miniblog/signin/')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignInForm(request=request, data=request.POST)
            if form.is_valid():
                u_name = form.cleaned_data['username']
                u_pass = form.cleaned_data['password']
                user = authenticate(username=u_name, password=u_pass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/miniblog/dashboard/')
        else:
            form = SignInForm()
        context = {
            'form': form
        }
        return render(request, 'miniblog/signin.html', context)
    else:
        return HttpResponseRedirect('/miniblog/dashboard/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congo! You are now the member of PORT CITY TROUBLE BLOG')
            user = form.save()
            group = Group.objects.get(name=Author)
            user.groups.add(group)
    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'miniblog/signup.html', context)


def addPost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddForm(request.POST)
            if form.is_valid():
                post_title = form.cleaned_data['title']
                post_des = form.cleaned_data['des']
                psts = BlogPost(title=post_title, des=post_des)
                psts.save()
                form = AddForm()
        else:
            form = AddForm()
        return render(request, 'miniblog/addpost.html',{'form': form})

    else:
        return HttpResponseRedirect('/miniblog/signin')

def updatePost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
           pi = BlogPost.objects.get(pk=id)
           form = AddForm(request.POST ,instance=pi)
           if form.is_valid():
            form.save()
    

        else:
            pi = BlogPost.objects.get(pk=id)
            form = AddForm(instance=pi)

        return render(request, 'miniblog/updatepost.html',{'form': form})

    else:
        return HttpResponseRedirect('/miniblog/signin')

def deletePost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = BlogPost.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/miniblog/dashboard')
        return render(request, 'miniblog/addpost.html')

    else:
        return HttpResponseRedirect('/miniblog/signin')