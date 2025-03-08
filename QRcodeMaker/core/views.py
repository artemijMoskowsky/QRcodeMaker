from django.shortcuts import render, redirect
from django.core.mail import send_mail
from QRcodeMaker.settings import EMAIL_HOST_USER
from django.http import HttpResponse
from user.models import CustomUser
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create your views here.
def render_home(request):
    if request.method == "POST":
        createQR = request.POST.get("create-QR")
        if createQR:
           return redirect("qrcodes/create_qrcode/")
        if request.user.is_authenticated:
            license = request.POST.get("subscribe")
            try:
                user = CustomUser.objects.get(pk = request.user.pk)
                user.licence_date = datetime.now() + relativedelta(seconds=1)
                user.licence = license
                user.save()
            except:
                pass
    return render(request = request, template_name = "core.html")

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        problem = request.POST.get('problem')
        recipient = 'artemij.mosckowsky.01062008@gmail.com'
        send_mail("Зворотній зв'язок",f"{name} написав відгук:\n{problem}\n\nПошта для зворотнього зв'язку {email}",EMAIL_HOST_USER,[recipient],fail_silently=False,) 
    return render(request, 'contacts.html')

