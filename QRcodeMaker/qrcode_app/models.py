from django.db import models
from user.models import CustomUser

class CreateQrcode(models.Model):
    image = models.ImageField(upload_to='images/')
    author_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    