from django.urls import path
from . import views
app_name='food'
urlpatterns = [
    path('', views.food_detail,name="food_detail"),
]