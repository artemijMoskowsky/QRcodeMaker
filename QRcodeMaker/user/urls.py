from django.urls import path

from .views import render_registation, render_login, render_logout

urlpatterns = [
    path('registration/', render_registation, name = "reg"),
    path('login/', render_login, name = "login"),
    path('logout/', render_logout, name='logout'),

]
