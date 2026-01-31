from django import forms
from .models import QRimg


class QrForm(forms.Form):
    link = forms.CharField()


class ImageForm(forms.ModelForm):
    class Meta:
        model = QRimg
        fields = ('title', 'image')
