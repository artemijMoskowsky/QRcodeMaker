from django.urls import path
from .views import render_create_qrcode, render_my_qrcodes, view_qrcode


urlpatterns = [
    path("create_qrcode/", render_create_qrcode),
    path("my_qrcodes/", render_my_qrcodes),
    path("view_qrcode/<int:id>", view_qrcode, name="view_qrcode")
]