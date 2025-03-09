from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser as User


def render_registation(request):
    context = {
        "name": [],
        "email": [],
        "password": []
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get("passwordConfirm")

        if User.objects.filter(username=username).exists():
            context["name"].append("Користувач з таким ім\'ям вже існує.")

        elif User.objects.filter(email=email).exists():
            context["email"].append("Користувач з таким email вже існує.")
        
        elif password != password_confirm:
            context["password"].append("Паролі не співпадають.")

        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            return redirect('login') 
    
    return render(request=request,template_name="registration/registration.html", context=context)

def render_login(request):
    context = {
        "error": []
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        
        else:
           context["error"].append("Неправильне ім\'я користувача або пароль.")

    return render(request=request,template_name="login/login.html", context=context)

def render_logout(request):
    logout(request)
    messages.success(request, 'Ви вийшли із системи.') 
    return redirect('login')  

 
def render_account(request):
    if request.user.is_authenticated:

        return render(request=request, template_name="account/account.html")
    return redirect("reg")