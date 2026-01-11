from django import forms

class QrForm(forms.Form):
    link = forms.CharField()
