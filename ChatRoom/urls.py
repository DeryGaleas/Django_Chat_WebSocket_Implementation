from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path("chat/", views.useless_chat, name="chat"),
    path("register/", views.register, name="register"),
    path("login/", views.loginUser, name="login"),
]
