from django.db import models
from user.models import CustomUser

class CreateQr(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='images')
    author_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    link = models.TextField()
    
    def __str__(self):
        return f"{self.link}"