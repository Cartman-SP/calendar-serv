from rest_framework import serializers
from .models import *



class UslugaSerializer(serializers.ModelSerializer):
    serviceCover = serializers.ImageField(required=False) # Добавляем поле для изображения

    class Meta:
        model = Usluga
        fields = ['id','user','name', 'cost', 'time', 'type', 'place_ammount', 'rent_ammount', 'pay_type', 'serviceCover']
        extra_kwargs = {
            'place_ammount': {'required': False},
            'rent_ammount': {'required': False},
        }

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'firstname', 'secondname', 'rank', 'avatar', 'serviceid', 'worktime', 'timetable', 'chilltime', 'user','days']


class Buisness_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buisness_Type
        fields = ['id', 'name']


class Buisness_sphereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buisness_Type
        fields = ['id', 'name']

class BranchSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)  # Используйте EmployeeSerializer для вложенной сериализации сотрудников
    avatar = serializers.ImageField(required=False)  # Добавляем поле изображения

    class Meta:
        model = Branch
        fields = '__all__'

    def create(self, validated_data):
        avatar = validated_data.pop('avatar', None)
        instance = super().create(validated_data)
        if avatar:
            instance.avatar = avatar
            instance.save()
        return instance