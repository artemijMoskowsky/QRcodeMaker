from django.urls import path
from .views import render_create_qrcode, render_my_qrcodes


urlpatterns = [
    path("create_qrcode/", render_create_qrcode),
    path("my_qrcodes/", render_my_qrcodes)
]