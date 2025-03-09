# QRcodeMaker
## Мета проекту:
Мета проекту - розробити сайт для створення qr кодів, на сайті присутня система акаунтів та підписок, та після закінчення часу підписки певні qr коди стають недоступними. Проект застосовує технології які можуть використовуватися у інших, більш великих проектах.
## Команда:
- [Moskowsky Artem - TeamLid](https://github.com/artemijMoskowsky)
- [Naumenko Nikita](https://github.com/Naumenko0Nikita)
- [Ovcharenko Julia](https://github.com/JuliaOvcharenko)
- [Sivaiev Matvii](https://github.com/MatviiSivaiev2009)

## Технології:
- Основний фреймворк - Django
- Мова програмування - Python

## Дизайн:
[Figma design](https://www.figma.com/design/THXxokVBx5AabxUlqFFraT/Django_practice?node-id=0-1&p=f&t=w1Ao5QVqjaxjg4ok-0)

## Наші додатки:
### core
У цьому додатку знаходятся домашня сторінка, та сторінка контактів. На домашній сторінці відбуваєтся зміна підписки. На сторінці контактів відбуваєтся відправка feedback.
### qrcode_app
У цьому додатку відбуваєтся створення, видалення, та відображення qr кодів.
### user
У цьому додатку відбуваєтся реєстрація та авторизація користувача.

## Я к встановити та запустити проект?
### Встановлення:
Завантажте проект
```bash
  git clone https://github.com/artemijMoskowsky/QRcodeMaker
```
Перейдіть до папки з проектом
```bash
  cd QRcodeMaker
```
Завантажте залежності
```bash
  pip install -r requirements.txt
```

### Запуск:
Перейдіть до головної папки сайту
```bash
  cd QRcodeMaker
```
Запустіть скрипт через manage.py
```bash
  python manage.py runserver [порт, але це не обов'язково]
```
