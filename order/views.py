from django.shortcuts import render

# Create your views here.
def order_detail(request):
    context={}
    return render(request,'order/order_detail.html',context)