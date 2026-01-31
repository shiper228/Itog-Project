from django.db import models


class QRimg(models.Model):
    title = models.CharField(max_length = 50, blank=True)
    image = models.ImageField(upload_to='media')
