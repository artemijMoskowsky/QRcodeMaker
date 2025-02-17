from django.shortcuts import render, redirect
from django.conf import settings
import time
import qrcode
from qrcode.image.styledpil import StyledPilImage
from .models import CreateQr
import io
from django.core.files.base import ContentFile
import datetime
from PIL import ImageColor
from qrcode.image.styledpil import SolidFillColorMask

# Create your views here.
def render_create_qrcode(request):
    img_name = None
    if request.method == "POST":
        if request.user.is_authenticated:

            my_qrcode = request.POST.get('data')
            qrcode_main_color = request.POST.get('color-input')
            qrcode_bg_color = request.POST.get('color-input-bg')
            html_logo = request.FILES.get('logo-input')
   
            if not qrcode_main_color:
                qrcode_main_color = "black"
            if not qrcode_bg_color:
                qrcode_bg_color = "white"
                print('white is bad')

            def hex_rgb(hex):
                return ImageColor.getrgb(hex)


            if my_qrcode:
                my_full_qrcode = qrcode.QRCode(
                    version = 1,
                    box_size = 10,
                    border = 4,
                    error_correction=qrcode.constants.ERROR_CORRECT_H)

                my_full_qrcode.add_data(my_qrcode)
                my_full_qrcode.make()

                img_name = 'qrcode' + str(time.time()) + '.png'
                image_colors = my_full_qrcode.make_image(fill_color = qrcode_main_color, back_color = qrcode_bg_color)
                print(type(html_logo))
                print(request.FILES)

                if html_logo:
                    print('image')
                    
                    image_colors = my_full_qrcode.make_image(image_factory=StyledPilImage, embeded_image_path=html_logo, color_mask = SolidFillColorMask(front_color=hex_rgb(qrcode_main_color), back_color=hex_rgb(qrcode_bg_color)))

                qrcode_io = io.BytesIO()
                image_colors.save(qrcode_io, format='PNG')

                add_qrcode = CreateQr.objects.create(
                    image=ContentFile(qrcode_io.getvalue(), name = img_name),
                    link = my_qrcode,
                    author_id = request.user,
                    date = datetime.datetime.today())

            return render(request, 'create_qrcode/create_qrcode.html', {'img_name': img_name})
        else:
            return redirect('reg')
    
    return render(request=request, template_name='create_qrcode/create_qrcode.html')
def render_my_qrcodes(request):
    return render(request=request, template_name='my_qrcodes/my_qrcodes.html')
