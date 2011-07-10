from django.http import HttpResponse
from django.utils import simplejson

from api.models import QrCode


def check_qrcode(request):
    qrcode_value = request.GET.get('qrcode', '')
    if not qrcode_value:
        return HttpResponse("Pass your qrcode string in get parameter 'qrcode'")

    try:
        qrcode = QrCode.objects.get(qrcode=qrcode_value)
        if qrcode.used:
            status = "This Qr Code was used"
        else:
            qrcode.used = True
            qrcode.save()
            status = "Ok"
    except QrCode.DoesNotExist:
        status = "Invalid Qr Code"
    return HttpResponse(status)