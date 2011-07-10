from django.db import models


class QrCode(models.Model):
    qrcode = models.CharField(blank=True, max_length=250)
    used = models.BooleanField(default=False)
