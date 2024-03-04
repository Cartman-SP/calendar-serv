from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    timezone = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.svg')
    password_changed_at = models.DateTimeField(null=True, blank=True)
    first_usluga = models.BooleanField(default=False)
    first_sotrudnik = models.BooleanField(default=False)
    first_filial = models.BooleanField(default=False)
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
 



class Buisness_Type(models.Model):
    name = models.CharField(max_length = 20)

class Branch(models.Model):
    type = models.ForeignKey(Buisness_Type, on_delete = models.CASCADE)

class Buisness_sphere(models.Model):
    name = models.CharField(max_length = 20)

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Привязка к пользователю
    firstname = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='employees/', null=True, blank=True)
    serviceid = models.CharField(max_length=256)  # Предположим, что это внешний ключ к модели услуги
    worktime = models.CharField(max_length=20)
    timetable = models.CharField(max_length=10)
    chilltime = models.CharField(max_length=20)
    days = models.CharField(max_length = 100)

class Branch(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    active_days = models.CharField(max_length=100)
    work_hours = models.CharField(max_length=100)
    timeout = models.CharField(max_length=100)
    business = models.CharField(max_length=255)
    phone = models.CharField(max_length = 20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Project(models.Model):
    name = models.CharField(max_length=128)
    timezone = models.CharField(max_length=128)
    currency = models.CharField(max_length=128)
    colour = models.CharField(max_length=128)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)

class BranchEmployee(models.Model):
    branch = models.ForeignKey(Branch, related_name='employees', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name='branches', on_delete=models.CASCADE)

class Image(models.Model):
    branch = models.ForeignKey(Branch, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='branch_images/', blank=True, null=True)  # Поле для изображения

class BranchType(models.Model):
    branch = models.ForeignKey(Branch, related_name='branches2', on_delete=models.CASCADE)
    type = models.ForeignKey(Buisness_Type, related_name='Buisness_Type', on_delete=models.CASCADE)


admin.site.register(Buisness_Type)
admin.site.register(Buisness_sphere)