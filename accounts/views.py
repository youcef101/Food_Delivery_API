from django.shortcuts import render,redirect
from .forms import CreateNewUser,ProfileUpdate,UserUpdate
from django.contrib.auth.models import Group,User
from .models import Customer
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash

from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib import messages
from .decorators import notLoggedUser
from django.contrib.auth.forms import PasswordChangeForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

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


def password_change(request):
    form = PasswordChangeForm(request.user)
    url=request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
          user = form.save()
          update_session_auth_hash(request, user)  # Important!
          messages.success(request, 'Your password was successfully updated!')
          return HttpResponseRedirect('/')
        else:
          messages.error(request, 'Please correct the error below.<br>'+ str(form.errors))
          return HttpResponseRedirect(url)
    
     
    context={'form':form}
    return render(request, 'auth/password_change.html',context)


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "auth/password_reset_email.html"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					#'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, settings.EMAIL_HOST_USER , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("password_reset_done")
	password_reset_form = PasswordResetForm()
	return render(request, template_name="auth/password_reset.html", context={"password_reset_form":password_reset_form})