import hashlib
import base64
import random
#import json

from django.http import Http404, HttpResponse
from django.conf import settings

from pygooglechart import QRChart

from serverqrgen.core.models import Customer, Participant


def generate_key():
    random.seed()
    secret_key = [b[0] for b in settings.SECRET_KEY]
    random.shuffle(secret_key)
    password = settings.SECRET_KEY + ''.join(secret_key)
    random.shuffle(secret_key)
    password += str(random.getrandbits(len(password))) + ''.join(secret_key)
    key = base64.urlsafe_b64encode(hashlib.sha256(password).digest())
    return str(key)


def submit_job(request):
    #if request.method not in ["POST", "PUT"]:
    #    return Http404()

    params = dict([item for item in request.REQUEST.items() if item[1]])

    customer = next(iter(Customer.objects.filter(id=params["customer"])),\
                         None)

    if customer is None:
        return Http404()

    participant = next(iter(Participant.objects.filter(\
                            email=params["email"])),\
                            None)

    #if participant:
    #    return Http404()

    participant = Participant.objects.create(customer=customer,
                                            first_name=params["first_name"],
                                            last_name=params["last_name"],
                                            email=params["email"],
                                            payload=params['payload'])

    participant.save()

    participant.code = generate_key()
    participant.save()

    # Create a 125x125 QR code chart
    chart = QRChart(250, 250)

    # Add the text
    chart.add_data(participant.code)

    # "Level H" error correction with a 0 pixel margin
    chart.set_ec('H', 0)

    # Download
    return HttpResponse(chart.get_url())
