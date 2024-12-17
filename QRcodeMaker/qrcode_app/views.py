from django.shortcuts import render

# Create your views here.
def render_create_qrcode(request):
    return render(request=request, template_name='create_qrcode/create_qrcode.html')

def render_my_qrcodes(request):
    return render(request=request, template_name='my_qrcode/my_qrcodes.html')
