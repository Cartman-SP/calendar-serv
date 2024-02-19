from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    timezone = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.svg')

    def save(self, *args, **kwargs):
        # Если изображение не было передано, используем изображение по умолчанию
        if not self.avatar:
            self.avatar = 'avatars/default_avatar.svg'
        super(Profile, self).save(*args, **kwargs)

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

class Reset_passwrod(models.Model):
    token = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='related_objects')
 

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Привязка к пользователю
    firstname = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='employees/', null=True, blank=True)
    serviceid = models.IntegerField()  # Предположим, что это внешний ключ к модели услуги
    worktime = models.CharField(max_length=20)
    timetable = models.CharField(max_length=10)
    chilltime = models.CharField(max_length=20)
    days = models.CharField(max_length = 100)