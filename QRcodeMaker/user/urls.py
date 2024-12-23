from django.urls import path

from .views import render_registation, render_login, render_logout, render_account

urlpatterns = [
    path('registration/', render_registation, name = "reg"),
    path('login/', render_login, name = "login"),
    path('logout/', render_logout, name = 'logout'),
    path('account/', render_account, name = "account")

]
