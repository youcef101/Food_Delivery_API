from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('', views.index,name="home"),
    path('contact/', views.contact,name="contact"),
    path('about-us/', views.about,name="about_us"),
]