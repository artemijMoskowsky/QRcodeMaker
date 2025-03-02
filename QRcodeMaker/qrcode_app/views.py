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
from django.urls import reverse
from django.http import HttpResponse

license_variants = {'free': 1, 'standart': 10, 'pro': 100}

# Create your views here.
def render_create_qrcode(request):
    img_name = None
    error_message = None
    if request.method == "POST":
        if request.user.is_authenticated:
            my_qrcode = request.POST.get('data')
            qrcode_main_color = request.POST.get('color-input')
            qrcode_bg_color = request.POST.get('color-input-bg')

            html_logo = request.FILES.get('logo-input')
            design_qrcode = request.POST.get('design-hidden')

            if not qrcode_main_color:
                qrcode_main_color = "black"
            if not qrcode_bg_color:
                qrcode_bg_color = "white"

            limited = request.user.licence
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

                def hex_rgb(hex):
                    return ImageColor.getrgb(hex)

                if my_qrcode:
                    my_full_qrcode = qrcode.QRCode(
                        version=1,
                        box_size=10,
                        border=4,
                        error_correction=qrcode.constants.ERROR_CORRECT_H
                    )

                    my_full_qrcode.add_data("")
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

                    user_qrcode = my_full_qrcode.make_image(image_factory=StyledPilImage)

                    qrcode_io = io.BytesIO()
                    user_qrcode.save(qrcode_io, format='PNG')

                    date = datetime.datetime.today()
                    CreateQr.objects.create(
                        image=ContentFile(qrcode_io.getvalue(), name=img_name),
                        link=my_qrcode,
                        author_id=request.user,
                        date=date
                    )

                    qr = CreateQr.objects.filter(link=my_qrcode, author_id=request.user, date=date).first()

                    my_full_qrcode.add_data(request.build_absolute_uri(reverse("view_qrcode", kwargs = {"id": qr.pk})))
                    my_full_qrcode.make()

                    img_name = 'qrcode' + str(time.time()) + '.png'

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

                    qr.image = ContentFile(qrcode_io.getvalue(), name=img_name)

                    qr.save()

                return render(request, 'create_qrcode/create_qrcode.html', {'img_name': img_name})
        else:
            return redirect('reg')

    return render(request, 'create_qrcode/create_qrcode.html')


def render_my_qrcodes(request):
    all_links = CreateQr.objects.filter(author_id = request.user)
    all_links = all_links[:license_variants[request.user.licence]]
    date = request.user.licence_date.replace(tzinfo=None)
    if date < datetime.datetime.now():
        all_links = [all_links[0]]

    all_links = [obj.id for obj in all_links]
    all_links = CreateQr.objects.filter(id__in = all_links)

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
            model = CreateQr.objects.get(id=int(delete_qrcode))
            model.delete_qrcode()


    return render(request, 'my_qrcodes/my_qrcodes.html', {'all_qrcodes': all_links})


def view_qrcode(request, id):
    qr = CreateQr.objects.filter(id = id).first()
    date = qr.author_id.licence_date.replace(tzinfo=None)
    try:
        if date > datetime.datetime.now():
            all_qr = CreateQr.objects.filter(author_id = qr.author_id)[:license_variants[qr.author_id.licence]]
            if qr in all_qr:
                return redirect(qr.link)
        else:
            all_qr = CreateQr.objects.filter(author_id = qr.author_id)
            if qr.id == all_qr[0].id:
                return redirect(qr.link)
    except:
        return HttpResponse(qr.link)