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

# Вы можете добавить другие поля в модель User, если это необходимо.
class Service(models.Model):
    # Название услуги
    name = models.CharField(max_length=255)
    # Стоимость услуги
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    # Длительность услуги
    duration = models.CharField(max_length=10)
    # Обложка услуги
    cover = models.ImageField(upload_to='covers/')  # Изменено название поля на "cover"
    # Тип записи
    record_type = models.CharField(max_length=10)
    # Тип оплаты
    payment_type = models.CharField(max_length=20)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
