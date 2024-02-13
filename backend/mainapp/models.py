from django.db import models

# models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    timezone = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)

class Usluga(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    place_ammount = models.CharField(max_length=50)
    rent_ammount = models.CharField(max_length=50)
    pay_type = models.CharField(max_length=50)
    serviceCover = models.ImageField(upload_to='service_covers/')