from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser as User


def render_registation(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Користувач з таким ім\'ям вже існує.')
            return redirect('reg')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Користувач з таким email вже існує.')
            return redirect('reg')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, 'Реєстрація пройшла успішно!')
        return redirect('login') 
    
    return render(request=request,template_name="registration/registration.html")

def render_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Вхід виконано успішно!')
            return redirect('/')
        
        else:
            messages.error(request, 'Неправильне ім\'я користувача або пароль.')
            return redirect('login')
           
    return render(request=request,template_name="login/login.html")

def render_logout(request):
    logout(request)
    messages.success(request, 'Ви вийшли із системи.') 
    return redirect('login')  

def render_account(request):
    return render(request=request, template_name="account/account.html")