from django.shortcuts import render, redirect
from django.core.mail import send_mail
from QRcodeMaker.settings import EMAIL_HOST_USER
from django.http import HttpResponse

# Create your views here.
def render_home(request):
    if request.method == "POST":
        createQR = request.POST.get("create-QR")
        print(createQR, 1)
        if createQR:
           return redirect("qrcodes/create_qrcode/")
        if request.user.is_authenticated:
            license = request.POST.get("subscribe")
            request.user.licence = license
    return render(request = request, template_name = "core.html")

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        problem = request.POST.get('problem')
        recipient = 'artemij.mosckowsky.01062008@gmail.com'
        send_mail("Зворотній зв'язок",f"{name} написав відгук:\n{problem}\n\nПошта для зворотнього зв'язку {email}",EMAIL_HOST_USER,[recipient],fail_silently=False,) 
    return render(request, 'contacts.html')


