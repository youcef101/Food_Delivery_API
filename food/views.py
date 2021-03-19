from django.shortcuts import render

# Create your views here.
def food_detail(request):
    context={}
    return render(request,'food/food_detail.html',context)