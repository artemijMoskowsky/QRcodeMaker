from django.shortcuts import render
from django.core.mail import send_mail
from QRcodeMaker.settings import EMAIL_HOST_USER
from django.http import HttpResponse
from user.models import CustomUser

# Create your views here.
def render_home(request):
    if request.method == "POST" and request.user.is_authenticated:
        license = request.POST.get("subscribe")
        try:
            user = CustomUser.objects.get(pk = request.user.pk)
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
