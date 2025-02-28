from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from dateutil.relativedelta import relativedelta
# Create your models here.


class CustomUser(AbstractUser):
    licence = models.CharField(max_length=255, blank=True, null=True)
    licence_date = models.DateTimeField(default=datetime.now() + relativedelta(months=1))

    def __str__(self):
        return self.username