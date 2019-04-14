from django.urls import path
from login import views


app_name = 'login'
urlpatterns = [
    path('', views.index, name="index"),
    #ex: /login/login
    path('login', views.login, name="login"),
    #ex: /login/register
    path('register', views.register, name="register"),
    #ex: /login/logout
    path('logout', views.logout, name="logout")
]