from django.shortcuts import render
from .models import ContactInfo,Setting,FAQ
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from food.models import Food,Category
from django.core.paginator import Paginator

# Create your views here.
@login_required(login_url='accounts:login')
def index(request):
    category=Category.objects.all()
    context={'category':category}
    return render(request,'home/index.html',context)

@login_required(login_url='accounts:login')
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
    
@login_required(login_url='accounts:login')
def about(request):
    setting=Setting.objects.get(id=1)
    context={'setting':setting}
    return render(request,'home/aboutus.html',context)

def category_food(request,id):
    category=Category.objects.all()
    cat_food=Food.objects.filter(category_id=id)
    paginator=Paginator(cat_food,8)
    page_number=request.GET.get('page')
    page_object=paginator.get_page(page_number)
    context={'page_object':page_object,'category':category}
    return render(request,'home/category_food.html',context)
    