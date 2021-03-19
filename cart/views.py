from django.shortcuts import render

# Create your views here.
def addtocart(request):
    context={}
    return render(request,'cart/cart.html',context)