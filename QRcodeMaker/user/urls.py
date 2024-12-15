from django.urls import path
from .views import render_registation

urlpatterns = [
    path('registration/', render_registation),

]
