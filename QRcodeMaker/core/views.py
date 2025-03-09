from django.shortcuts import render, redirect
from django.core.mail import send_mail
from QRcodeMaker.settings import EMAIL_HOST_USER
from django.http import HttpResponse
from user.models import CustomUser
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create your views here.
# створюємо функцію відображення домашньої сторінки
def render_home(request):
    # перевіряємо чи є запрос дорівнює POST
    if request.method == "POST":
        # отримуємо значення кнопки створення QR коду
        createQR = request.POST.get("create-QR")
        # якщо натиснута кнопка
        if createQR:
           # перенаправляємо користувача на сторінку створення QR кодів
           return redirect("qrcodes/create_qrcode/")
        # перевіряємо чи автентифікований користувач
        if request.user.is_authenticated:
            # отримуємо значення підписки
            license = request.POST.get("subscribe")
            
            try:
                # отримумо користуача з бази даних
                user = CustomUser.objects.get(pk = request.user.pk)
                # встановлюємо дату закінчення ліцензії на моточний момент 1 секунда
                user.licence_date = datetime.now() + relativedelta(seconds=1)
                # встановлюємо значення ліцензії
                user.licence = license
                # зберігаємо оновлені дані користувача в базу
                user.save()
            except:
                pass
    # повертаємо шаблон головної сторінки
    return render(request = request, template_name = "core.html")

# створюємо функцію для обробки форми зворотного зв'язку
def contacts(request):
    # перевіряємо чи запит дорівнює POST
    if request.method == 'POST':
        # отримуємо ім'я користувача з форми
        name = request.POST.get('name')
        # отримуємо email користувача
        email = request.POST.get('email')
        # отримуємо повідомлення про проблему
        problem = request.POST.get('problem')
        # встановлюємо email отримувача
        recipient = 'artemij.mosckowsky.01062008@gmail.com'
        #відправляємо email з повідомленням
        send_mail("Зворотній зв'язок",f"{name} написав відгук:\n{problem}\n\nПошта для зворотнього зв'язку {email}",EMAIL_HOST_USER,[recipient],fail_silently=False,)
    # повертаємо шаблон сторінки зворотного зв'язку
    return render(request, 'contacts.html')

