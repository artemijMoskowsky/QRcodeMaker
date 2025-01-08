from django.shortcuts import render
from django.core.mail import send_mail
from QRcodeMaker.settings import EMAIL_HOST_USER

# Create your views here.
def render_home(request):
    return render(request = request, template_name = "core.html")

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        problem = request.POST.get('problem')
        recipient = 'artemij.mosckowsky.01062008@gmail.com'
        send_mail("Зворотній зв'язок",f"{name} написав відгук:\n{problem}\n\nПошта для зворотнього зв'язку {email}",EMAIL_HOST_USER,[recipient],fail_silently=False,) 
    return render(request, 'contacts.html')



    