from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from dateutil.relativedelta import relativedelta
# Create your models here.

# Створюємо власний класс користувача
class CustomUser(AbstractUser):
    # Створюємо поле для ліцензії
    licence = models.CharField(max_length=255, blank=True, null=True)
    # Створюємо поле дати завершення ліцензії
    licence_date = models.DateTimeField(default=datetime.now() + relativedelta(months=1))

    # Задаємо стандартне строкове відображення
    def __str__(self):
        # Повертаємо ім'я користувача
        return self.username