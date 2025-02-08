from django.shortcuts import render
from django.conf import settings
import time
import qrcode
import os
from .models import CreateQr


# Create your views here.
def render_create_qrcode(request):
    if request.method == "POST":
        my_qrcode = request.POST.get('data')
        print(my_qrcode)
        
        img = qrcode.make(my_qrcode)
        img_name = 'qrcode' + str(time.time()) + '.png'
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)
        img.save(img_path)
        
        return render(request, 'create_qrcode/create_qrcode.html', {'img_name': img_name})

    return render(request=request, template_name='create_qrcode/create_qrcode.html')
def render_my_qrcodes(request):
    return render(request=request, template_name='my_qrcodes/my_qrcodes.html')
