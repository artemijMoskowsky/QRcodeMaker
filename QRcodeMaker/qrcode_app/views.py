from django.shortcuts import render, redirect
from django.conf import settings
import time
import qrcode
from qrcode.image.styledpil import StyledPilImage
from .models import CreateQr, CustomUser
import io
from django.core.files.base import ContentFile
import datetime
from PIL import ImageColor
from qrcode.image.styledpil import SolidFillColorMask
from qrcode.image.styles.moduledrawers.pil import SquareModuleDrawer, CircleModuleDrawer, GappedSquareModuleDrawer, RoundedModuleDrawer
from django.contrib import messages

# Create your views here.
def render_create_qrcode(request):
    img_name = None
    error_message = None
    if request.method == "POST":
        if request.user.is_authenticated:

            limited = request.user.licence
            license_variants = {'free': 1, 'standart': 10, 'pro': 100}
            limit = license_variants.get(limited, None)
            user_qrcodes = CreateQr.objects.filter(author_id = request.user).count()
            
            if limit and user_qrcodes >= limit:
                error_message = messages.error(request, 'Ваш тариф не дозволяє створювати більше qr-кодів.')
                return render(request, 'create_qrcode/create_qrcode.html') 

            else:
                my_qrcode = request.POST.get('data')
                qrcode_main_color = request.POST.get('color-input')
                qrcode_bg_color = request.POST.get('color-input-bg')
                html_logo = request.FILES.get('logo-input')
                design_qrcode = request.POST.get('design-hidden')

                if not qrcode_main_color:
                    qrcode_main_color = "black"
                if not qrcode_bg_color:
                    qrcode_bg_color = "white"
                    print('white is bad')

                def hex_rgb(hex):
                    return ImageColor.getrgb(hex)

                if my_qrcode:
                    my_full_qrcode = qrcode.QRCode(
                        version=1,
                        box_size=10,
                        border=4,
                        error_correction=qrcode.constants.ERROR_CORRECT_H
                    )

                    my_full_qrcode.add_data(my_qrcode)
                    my_full_qrcode.make()

                    img_name = 'qrcode' + str(time.time()) + '.png'

                    module_drawer = SquareModuleDrawer()
                    if design_qrcode:
                        if design_qrcode == 'circle':
                            module_drawer = CircleModuleDrawer()
                        elif design_qrcode == 'square':
                            module_drawer = GappedSquareModuleDrawer(size_ratio=0.8)
                        elif design_qrcode == 'border':
                            module_drawer = RoundedModuleDrawer()

                    user_qrcode = my_full_qrcode.make_image(
                        image_factory=StyledPilImage,
                        embeded_image_path=html_logo,
                        color_mask=SolidFillColorMask(
                            front_color=hex_rgb(qrcode_main_color),
                            back_color=hex_rgb(qrcode_bg_color)
                        ),
                        module_drawer=module_drawer
                    )

                    qrcode_io = io.BytesIO()
                    user_qrcode.save(qrcode_io, format='PNG')

                    CreateQr.objects.create(
                        image=ContentFile(qrcode_io.getvalue(), name=img_name),
                        link=my_qrcode,
                        author_id=request.user,
                        date=datetime.datetime.today()
                    )

                return render(request, 'create_qrcode/create_qrcode.html', {'img_name': img_name})
        else:
            return redirect('reg')

    return render(request, 'create_qrcode/create_qrcode.html')


def render_my_qrcodes(request):
    all_links = CreateQr.objects.filter(author_id = request.user)

    if not request.user.is_authenticated:
        return redirect('reg')

    if request.method == "POST":
        date_filter = request.POST.get('date-filter')
        link_filter = request.POST.get('link-filter')
        delete_qrcode = request.POST.get('button-delete')

        if date_filter:
            all_links = all_links.order_by("-date") 

        elif link_filter:
            all_links = all_links.order_by("link")

        elif delete_qrcode:
            CreateQr.objects.filter(id=int(delete_qrcode)).delete()


    return render(request, 'my_qrcodes/my_qrcodes.html', {'all_qrcodes': all_links})