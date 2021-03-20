from django.shortcuts import render
from .forms import CreateNewUser,ProfileUpdate,UserUpdate
from django.contrib.auth.models import Group,User
from .models import Customer
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .decorators import notLoggedUser

# Create your views here.
@notLoggedUser
def register(request):
    if request.method=='POST':
        form=CreateNewUser(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            user=form.save()
            instance=User.objects.get(username=username)
            group=Group.objects.get(name='customer')
            user=user.groups.add(group)
            Customer.objects.create(user=instance)
            messages.success(request,username +' Successfully created')
            return HttpResponseRedirect(reverse('accounts:login'))


    context={}
    return render(request,'auth/register.html',context)
@notLoggedUser
def userLogin(request):
    if request.method=='POST':
       username=request.POST.get('username')
       password=request.POST.get('password')
       user=authenticate(request,username=username,password=password)
       if user is not None:
           login(request,user)
           return HttpResponseRedirect(reverse('home:home'))
           messages.success(request,'hello '+username)
       else:
            messages.warning(request,'passwoed or username didnt match')
    context={}
    return render(request,'auth/login.html',context)

def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))

def profile(request):
    current_user=request.user
    profile=Customer.objects.get(user_id=current_user.id)
    context={'profile':profile}
    return render(request,'auth/user_profile.html',context)

def user_update(request):
    current_user=request.user
    profile=Customer.objects.get(user_id=current_user.id)
    if request.method=='POST':
        profile_form=ProfileUpdate(request.POST,request.FILES,instance=profile)
        user_form=UserUpdate(request.POST,instance=current_user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return HttpResponseRedirect(reverse('accounts:profile'))
    else:
        profile_form=ProfileUpdate(request.POST)
        user_form=UserUpdate(request.POST)
    context={#'profile_form':profile_form,
              #'user_form': user_form
             }
    return render(request,'auth/user_update.html',context)