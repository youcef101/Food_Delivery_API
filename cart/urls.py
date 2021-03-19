from django.urls import path
from . import views
app_name='cart'
urlpatterns = [
    path('', views.addtocart,name="add_to_cart"),
]
