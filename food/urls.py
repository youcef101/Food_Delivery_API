from django.urls import path
from . import views
from . import api
app_name='food'
urlpatterns = [
    path('', views.food_detail,name="food_detail"),
    #----api----#
    path('food_api/', api.food_list_api,name="food_list_api"),
    path('food_api/<int:id>', api.get_food_api,name="get_food_api"),
    path('category_api/', api.category_list_api,name="category_list_api"),
    path('category_api/<int:id>', api.get_category_api,name="get_category_api"),
    path('category_api/<int:id>', api.get_category_api,name="get_category_api"),
    path('add_food_api/', api.add_food_api,name="add_food_api"),
    path('add_category_api/', api.add_category_api,name="add_category_api"),
    path('edit_category_api/<int:id>', api.edit_category_api,name="edit_category_api"),
    path('delete_category_api/<int:id>', api.delete_category_api,name="delete_category_api"),

]