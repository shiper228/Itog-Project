from django.shortcuts import render
from itog_app.QR import QrCode
from itog_app.forms import *
def welcome_page(request):
    return render(request, 'welcome.html')


def generate_page(request):
    qr_url = None
    if request.method == 'POST':
        link = request.POST.get('link', '')

        if link:
            qr = QrCode(link)
            qr.make_qr_img()

            result = qr.save_qr_to_static()

            if result:
                qr_url = f"/static/qr_{result.get('qr_number', 1)}.png"

    return render(request, 'generate.html', {'qr_url': qr_url})


def new_page(request):
    return render(request, 'new.html')


def history_page(request):
    return render(request, 'history.html')
