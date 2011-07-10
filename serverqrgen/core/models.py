from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    token = models.CharField(max_length=255)


USER_STATUS_CHOICES = (
    ('N', 'New'),
    ('R', 'Registered'),
    ('U', 'Unpaid')
)


class Participant(models.Model):
    customer = models.ForeignKey(Customer)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    payload = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=USER_STATUS_CHOICES,
                                default='N')
    code = models.CharField(max_length=255, blank=True, null=True)
