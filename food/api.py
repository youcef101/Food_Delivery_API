from .serializers import FoodSerializer,CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Food,Category

@api_view(['GET'])
def food_list_api(request):
    all_food=Food.objects.all()
    data=FoodSerializer(all_food,many=True).data
    context={'data':data}
    return Response(context)


@api_view(['GET'])
def get_food_api(request,id):
    food=Food.objects.get(id=id)
    data=FoodSerializer(food,many=False).data
    context={'data':data}
    return Response(context)

@api_view(['GET'])
def category_list_api(request):
    all_category=Category.objects.all()
    data=CategorySerializer(all_category,many=True).data
    context={'data':data}
    return Response(context)

@api_view(['GET'])
def get_category_api(request,id):
    category=Category.objects.get(id=id)
    data=CategorySerializer(category,many=False).data
    context={'data':data}
    return Response(context)

@api_view(['POST'])
def add_food_api(request):
    serializer=FoodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    context={'data':data}
    return Response(context)

@api_view(['POST'])
def add_category_api(request):
    serializer=CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def edit_category_api(request,id):
    category=Category.objects.get(id=id)
    serializer=CategorySerializer(instance=category,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['delete'])
def delete_category_api(request,id):
    category=Category.objects.get(id=id).delete()
    return Response(' item Successfully deleted!')