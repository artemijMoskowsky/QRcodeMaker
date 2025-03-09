from django.urls import path
from .views import render_home, contacts
# Визначаємо шляхи
urlpatterns = [
    # Головна сторінка
    path('', render_home),
    # Сторінка контактів
    path('contacts/', contacts)
] 