from django.shortcuts import render

# Create your views here.
def render_registation(request):
    return render(request=request,template_name="registration/registration.html")