from rest_framework import serializers
from .models import Usluga



class UslugaSerializer(serializers.ModelSerializer):
    serviceCover = serializers.ImageField(required=False) # Добавляем поле для изображения

    class Meta:
        model = Usluga
        fields = ['user','name', 'cost', 'time', 'type', 'place_ammount', 'rent_ammount', 'pay_type', 'serviceCover']
        extra_kwargs = {
            'place_ammount': {'required': False},
            'rent_ammount': {'required': False},
        }