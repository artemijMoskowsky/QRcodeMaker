from django.db import models
from user.models import CustomUser

# Створюємо модель qr коду
class CreateQr(models.Model):
    # Задаємо поле id
    id = models.IntegerField(primary_key=True)
    # Задаємо поле для зображення
    image = models.ImageField(upload_to='images')
    # Задаємо поле для автора
    author_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Задаємо поле для дати створення
    date = models.DateField()
    # Задаємо поле для змісту qr коду
    link = models.TextField()

    # Функція видалення qr коду
    def delete_qrcode(self):
        # Видаляємо зображення з media файлів
        self.image.delete()
        # Видаляємо qr код з бази даних
        super(CreateQr, self).delete()
    
    # Створюмо стандратне строкове відображення
    def __str__(self):
        # Повертаємо зміст qr коду
        return f"{self.link}"

