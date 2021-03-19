from django.shortcuts import render
from .models import ContactInfo,Setting,FAQ
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    
    context={}
    return render(request,'home/index.html',context)

def contact(request):
    faq=FAQ.objects.all()
    contact_info=ContactInfo.objects.get(id=1)
    url=request.META.get('HTTP_REFERER')
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            subject=form.cleaned_data.get('subject')
            email=form.cleaned_data.get('email')
            message=form.cleaned_data.get('message')
            send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
            )
            form.save()
            return HttpResponseRedirect(url)
    else:
        form=ContactForm()
    context={'contact_info':contact_info,'faq':faq}
    return render(request,'home/contact.html',context)

def about(request):
    setting=Setting.objects.get(id=1)
    context={'setting':setting}
    return render(request,'home/aboutus.html',context)