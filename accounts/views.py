from django.shortcuts import render

# Create your views here.
def register(request):
    context={}
    return render(request,'auth/register.html',context)

def userLogin(request):
    context={}
    return render(request,'auth/login.html',context)