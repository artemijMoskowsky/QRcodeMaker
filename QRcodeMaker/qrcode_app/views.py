from django.shortcuts import render
from django.conf import settings
import time
import qrcode
import os
from .models import CreateQr
import io
from django.core.files.base import ContentFile
import datetime


# Create your views here.
def render_create_qrcode(request):
    ing_name = None
    if request.method == "POST":
        if request.user.is_authenticated:
            my_qrcode = request.POST.get('data')
            if my_qrcode:
                print(my_qrcode)
                
                img = qrcode.make(my_qrcode)
                img_name = 'qrcode' + str(time.time()) + '.png'
                # img_path = os.path.join(settings.MEDIA_ROOT, img_name)
                qrcode_io = io.BytesIO()
                img.save(qrcode_io, format='PNG')

                add_qrcode = CreateQr.objects.create(
                    image=ContentFile(qrcode_io.getvalue(), name = img_name),
                    link = my_qrcode,
                    author_id = request.user,
                    date = datetime.datetime.today())

            return render(request, 'create_qrcode/create_qrcode.html', {'img_name': img_name})

    return render(request=request, template_name='create_qrcode/create_qrcode.html')
def render_my_qrcodes(request):
    return render(request=request, template_name='my_qrcodes/my_qrcodes.html')
