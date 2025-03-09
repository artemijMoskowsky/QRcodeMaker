from django.shortcuts import render, redirect
from django.conf import settings
import time
import qrcode
from qrcode.image.styledpil import StyledPilImage
from .models import CreateQr, CustomUser
import io
from django.core.files.base import ContentFile
import datetime
from PIL import ImageColor
from qrcode.image.styledpil import SolidFillColorMask
from qrcode.image.styles.moduledrawers.pil import SquareModuleDrawer, CircleModuleDrawer, GappedSquareModuleDrawer, RoundedModuleDrawer
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse

# Задаємо обмеження для підписок
license_variants = {'free': 1, 'standart': 10, 'pro': 100}

# Створюємо функцію відображення для сторінки створення qr коду
def render_create_qrcode(request):
    # Задаємо ім'я картинки за замовчуванням
    img_name = None
    # Якщо відбувся POST запит на сервер:
    if request.method == "POST":
        # Якщо користувач авторизований:
        if request.user.is_authenticated:
            # Отримуємо посилання qr коду
            my_qrcode = request.POST.get('data')
            # Отримуємо колір qr коду
            qrcode_main_color = request.POST.get('color-input')
            # Отримуємо колір заднього фону qr коду
            qrcode_bg_color = request.POST.get('color-input-bg')

            # Отримуємо логотип qr коду
            html_logo = request.FILES.get('logo-input')
            # Отримуємо дизайн qr коду
            design_qrcode = request.POST.get('design-hidden')

            # Якщо колір не був задан:
            if not qrcode_main_color:
                # Ставимо за замовчуванням на чорний
                qrcode_main_color = "black"
            # Якщо колір заднього фону не був задан:
            if not qrcode_bg_color:
                # Ставимо за замовчуванням на білий
                qrcode_bg_color = "white"

            # Отримуємо підписку користувача для того щоб дізнатись ліміт qr кодів
            limited = request.user.licence
            # Отримуємо ліміт за підпискою користувача
            limit = license_variants.get(limited, None)
            # Отримуємо кількість qr кодів цього користувача
            user_qrcodes = CreateQr.objects.filter(author_id = request.user).count()
            
            # Якщо кількість qr кодів досягла ліміту
            if limit and user_qrcodes >= limit:
                # Повідомляємо користувача про те, що він не може створити qr код
                messages.error(request, 'Ваш тариф не дозволяє створювати більше qr-кодів.')
                # Прериваємо виконання функції відображаючи сторінку
                return render(request, 'create_qrcode/create_qrcode.html') 
            # Якщо кількість qr кодів не досягла ліміту
            else:
                my_qrcode = request.POST.get('data')
                qrcode_main_color = request.POST.get('color-input')
                qrcode_bg_color = request.POST.get('color-input-bg')
                html_logo = request.FILES.get('logo-input')
                design_qrcode = request.POST.get('design-hidden')

                if not qrcode_main_color:
                    qrcode_main_color = "black"
                if not qrcode_bg_color:
                    qrcode_bg_color = "white"

                # Функція переводу hex до rgb
                def hex_rgb(hex):
                    return ImageColor.getrgb(hex)

                # Якщо посилання qr коду було задано:
                if my_qrcode:
                    # Створюємо об'єкт qr коду
                    my_full_qrcode = qrcode.QRCode(
                        version=1,
                        box_size=10,
                        border=4,
                        error_correction=qrcode.constants.ERROR_CORRECT_H
                    )
                    # Додаємо пусте посилання
                    my_full_qrcode.add_data("")
                    # Генеруємо qr код
                    my_full_qrcode.make()

                    # Задаємо ім'я для qr коду
                    img_name = 'qrcode' + str(time.time()) + '.png'

                    # Задаємо стандартне значення module_drawer
                    module_drawer = SquareModuleDrawer()
                    # Якщо був задан дизайн:
                    if design_qrcode:
                        # Задаємо дизайн "коло"
                        if design_qrcode == 'circle':
                            module_drawer = CircleModuleDrawer()
                        # Задаємо дизайн "квадрат"
                        elif design_qrcode == 'square':
                            module_drawer = GappedSquareModuleDrawer(size_ratio=0.8)
                        # Задаємо дизайн "закруглений"
                        elif design_qrcode == 'border':
                            module_drawer = RoundedModuleDrawer()

                    # Генеруємо зображення (стокове, без прийняття усіх раніше заданих параметрів)
                    user_qrcode = my_full_qrcode.make_image(image_factory=StyledPilImage)

                    # Створюємо тимчасовий буфер
                    qrcode_io = io.BytesIO()
                    # Зберігаємо qr код в буфер
                    user_qrcode.save(qrcode_io, format='PNG')

                    # Зберігаємо сьогоднішню дату
                    date = datetime.datetime.today()
                    # Створюємо qr код у базі даних
                    CreateQr.objects.create(
                        image=ContentFile(qrcode_io.getvalue(), name=img_name),
                        link=my_qrcode,
                        author_id=request.user,
                        date=date
                    )
                    # Отримуємо щойно створений qr код з бази даних
                    qr = CreateQr.objects.filter(link=my_qrcode, author_id=request.user, date=date).first()

                    # Додаємо до qr коду посилання на обїект у базі даних
                    my_full_qrcode.add_data(request.build_absolute_uri(reverse("view_qrcode", kwargs = {"id": qr.pk})))
                    # Генеруємо qr код
                    my_full_qrcode.make()

                    # Генеруємо зображення (вже з усіма параметрами)
                    user_qrcode = my_full_qrcode.make_image(
                        image_factory=StyledPilImage,
                        embeded_image_path=html_logo,
                        color_mask=SolidFillColorMask(
                            front_color=hex_rgb(qrcode_main_color),
                            back_color=hex_rgb(qrcode_bg_color)
                        ),
                        module_drawer=module_drawer
                    )

                    # Знову створюємо буфер
                    qrcode_io = io.BytesIO()
                    # Зберігаємо зображення в буфер
                    user_qrcode.save(qrcode_io, format='PNG')

                    # Зберігаємо зображення до запису у базі даних
                    qr.image = ContentFile(qrcode_io.getvalue(), name=img_name)
                    # Зберігаємо зміни
                    qr.save()
                # Рендеримо сторінку передаючи ім'я qr коду
                return render(request, 'create_qrcode/create_qrcode.html', {'img_name': img_name})
        # Якщо користувач не зареєстрований
        else:
            # Переносимо користувача на сторінку реєстрації
            return redirect('reg')
    # Рендеримо сторінку
    return render(request, 'create_qrcode/create_qrcode.html')

# Створюємо функцію відображення для сторінки показу усіх qr кодів
def render_my_qrcodes(request):
    # Якщо користувач не авторизований:
    if not request.user.is_authenticated:
        # Переносимо користувача на сторінку реєстрації
        return redirect('reg')
    # Отримуємо усі qr коди користувача з бази даних
    all_links = CreateQr.objects.filter(author_id = request.user)
    # Обрізаємо qr коди відштовхуючись від підписки користувача
    all_links = all_links[:license_variants[request.user.licence]]
    # Отримуємо дату кінця ліцензії
    date = request.user.licence_date.replace(tzinfo=None)
    # Якщо дата закінчення вже настала
    if date < datetime.datetime.now():
        # Зберігаємо у списку лише перший qr код
        all_links = [all_links[0]]
    # Переводимо цей список у список id qr кодів
    all_links = [obj.id for obj in all_links]
    # Занходимо усі qr коди зі списка їх id
    all_links = CreateQr.objects.filter(id__in = all_links)

    # Якщо прийшов POST запит (тут це запит на сотрування, або видалення)
    if request.method == "POST":
        # Отримуємо чи є фільтрація по даті у запиту
        date_filter = request.POST.get('date-filter')
        # Отримуємо чи є фільтрація по посилання у запиту
        link_filter = request.POST.get('link-filter')
        # Отримуємо чи є запит на видалення qr коду
        delete_qrcode = request.POST.get('button-delete')

        # Якщо був запит на фільтрацію по даті:
        if date_filter:
            # Фільтруємо qr коди по даті перед відображенням на сторінці
            all_links = all_links.order_by("-date") 

        # Якщо був запит на фільтрацію по посиланню:
        elif link_filter:
            # Фільтруємо qr коди по посиланню перед відображенням на сторінці
            all_links = all_links.order_by("link")

        # Якщо був запит на видалення:
        elif delete_qrcode:
            # Отримуємо qr код з бази даних по id (id отримуєтся через запит)
            model = CreateQr.objects.get(id=int(delete_qrcode))
            # Видаляємо qr код
            model.delete_qrcode()

    # Рендеримо сторінку передаючи на неї усі доступні qr коди
    return render(request, 'my_qrcodes/my_qrcodes.html', {'all_qrcodes': all_links})

# Створюємо функцію, що буде переносити користувача на інше посилання при заході на неї (при сканувані qr коди, ручного способу через посилання звернутися до запису у базі даних)
def view_qrcode(request, id):
    # Отримуємо qr код за бази даних
    qr = CreateQr.objects.filter(id = id).first()
    # Отримуємо дату завершення підписки автора цього qr коду
    date = qr.author_id.licence_date.replace(tzinfo=None)
    # try - except тут потрібен для того, якщо у qr коді буде текст, а не посилання, тоді замість переносу за посилання, просто відобразится текст
    try:
        # Якщо підписка ще дійсна:
        if date > datetime.datetime.now():
            # Отримуємо усі qr коди цього автора, та обрізаємо за підпискою
            all_qr = CreateQr.objects.filter(author_id = qr.author_id)[:license_variants[qr.author_id.licence]]
            # Якщо цей qr код серед тих що доступні:
            if qr in all_qr:
                # Пробуємо перейти за посиланням (якщо qr код з текстом, а не посиланням, спрацює except)
                return redirect(qr.link)
        else:
            # Якщо підписка не є дійсною:
            all_qr = CreateQr.objects.filter(author_id = qr.author_id)
            # Перевіряємо чи є цей qr код єдиним доступним (за бесплатною підпискою)
            if qr.id == all_qr[0].id:
                # Пробуємо перейти за посиланням (якщо qr код з текстом, а не посиланням, спрацює except)
                return redirect(qr.link)
    except:
        # Повертаємо текст, якщо qr код не містив у собі посилання
        return HttpResponse(qr.link)