from django.urls import path
from . import views
app_name='accounts'
urlpatterns = [
    path('register/', views.register,name="register"),
    path('login/', views.userLogin,name="login"),
    path('logout/', views.userLogout,name="logout"),
    path('profile/', views.profile,name="profile"),
    path('user_update/', views.user_update,name="user_update"),
    path('password/', views.password_change, name='password_change'),
    path("password_reset/", views.password_reset_request, name="password_reset")
]