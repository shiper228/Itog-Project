from django.shortcuts import render
from itog_app.QR import QrCode
from itog_app.forms import QrForm
def welcome_page(request):
    return render(request, 'welcome.html')


def generate_page(request):
    context = {}
    if request.method == "POST":
        form = QrForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            qr = QrCode(link)
            qr.make_qr_img()
            qr.show_qrcode()
            context['form'] = form
    else:
        form = QrForm()
        context['form'] = form
    return render(request, 'generate.html', context)




def history_page(request):
    return render(request, 'history.html')
