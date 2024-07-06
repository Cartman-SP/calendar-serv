from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, unique = True)
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

class Project(models.Model):
    name = models.CharField(max_length=128)
    timezone = models.CharField(max_length=128)
    currency = models.CharField(max_length=128)
    colour = models.CharField(max_length=128)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)




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
    project = models.ForeignKey(Project,on_delete = models.CASCADE)
    employees = models.CharField(max_length=50, default = '')

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
    project = models.ForeignKey(Project,on_delete = models.CASCADE)
    daystime = models.JSONField(default=dict)

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
    project = models.ForeignKey(Project,on_delete = models.CASCADE)
    employees_id = models.CharField(max_length = 1000)

class BranchEmployee(models.Model):
    branch = models.ForeignKey(Branch, related_name='employees', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name='branches', on_delete=models.CASCADE)

class Image(models.Model):
    branch = models.ForeignKey(Branch, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='branch_images/', blank=True, null=True)  # Поле для изображения

class BranchType(models.Model):
    branch = models.ForeignKey(Branch, related_name='branches2', on_delete=models.CASCADE)
    type = models.ForeignKey(Buisness_Type, related_name='Buisness_Type', on_delete=models.CASCADE)

class Widget(models.Model):
    language = models.CharField(max_length=100)
    design = models.CharField(max_length=100)
    text = models.TextField()
    plashka = models.CharField(max_length=100)
    back = models.CharField(max_length=100)
    main = models.CharField(max_length=100)
    theme = models.BooleanField(default=False)
    ogranichenie = models.CharField(max_length=100)
    interval = models.CharField(max_length=100)
    cancellation = models.BooleanField(default=False)
    employee = models.BooleanField(default=False)
    company = models.BooleanField(default=False)
    feedback = models.BooleanField(default=False)
    vklink = models.CharField(max_length=100)
    isvk = models.BooleanField(default=False)
    whatsapplink = models.CharField(max_length=100)
    iswhatsapp = models.BooleanField(default=False)
    instagramlink = models.CharField(max_length=100)
    isinstagram = models.BooleanField(default=False)
    telegramlink = models.CharField(max_length=100)
    istelegram = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    branches = models.CharField(max_length=10000)
    telegramtoken = models.CharField(max_length=5000)
    buttonname = models.CharField(max_length=25)
    hellomessage = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True) #НОВОЕ ПОЛЕ ДЛЯ ОТСЛЕЖИВАНИЯ СОЗДАНИЯ И ОБНОВЛЕНИЯ ВИДЖЕТА 
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='unique_user_widget_name')
        ]



class WidgetImage(models.Model):
    widget = models.ForeignKey(Widget, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='widget_images')

class WidgetLoad(models.Model):
    widget = models.ForeignKey(Widget, on_delete=models.CASCADE)
    load_time = models.DateTimeField(auto_now_add=True)

class Client(models.Model):
    firstname = models.CharField(max_length=128)
    secondname = models.CharField(max_length=128)
    mail = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    date = models.CharField(max_length=128)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Application(models.Model):
    status = models.CharField(max_length=128)
    data = models.CharField(max_length=256)
    usluga = models.ForeignKey(Usluga,on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    time = models.DateTimeField()

class Integration(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    description = models.CharField(max_length=2000)
    status = models.BooleanField(default=False)
    date = models.CharField(max_length=2000)

class IntegrationLink(models.Model):
    integration = models.ForeignKey(Integration,on_delete = models.CASCADE)
    widget = models.ForeignKey(Widget,on_delete = models.CASCADE)

class Promo(models.Model):
    admin_name = models.CharField(max_length=250)
    client_name = models.CharField(max_length=250)
    start_date = models.CharField(max_length=250)
    end_date = models.CharField(max_length=250)
    promo_text = models.CharField(max_length=16)
    sale = models.IntegerField()
    activate = models.IntegerField()

class UCode(models.Model):
    widget = models.ForeignKey(Widget,on_delete=models.CASCADE)
    before_head = models.CharField(max_length=2000)
    before_body = models.CharField(max_length=2000)


admin.site.register(Integration)
admin.site.register(Buisness_Type)
admin.site.register(Buisness_sphere)


