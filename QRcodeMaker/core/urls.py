from django.urls import path
from .views import render_home, contacts

urlpatterns = [
    path('', render_home),
    path('contacts/', contacts)
] 