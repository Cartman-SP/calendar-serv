from rest_framework import serializers
from .models import *



class UslugaSerializer(serializers.ModelSerializer):
    serviceCover = serializers.ImageField(required=False) # Добавляем поле для изображения
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())  # Добавляем поле проекта

    class Meta:
        model = Usluga
        fields = ['id','user','name', 'cost', 'time', 'type', 'place_ammount', 'rent_ammount', 'pay_type', 'serviceCover', 'project']
        extra_kwargs = {
            'place_ammount': {'required': False},
            'rent_ammount': {'required': False},
        }

class EmployeeSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())  # Добавляем поле проекта

    class Meta:
        model = Employee
        fields = ['id', 'firstname', 'secondname', 'rank', 'avatar', 'serviceid', 'worktime', 'timetable', 'chilltime', 'user','days', 'project']


class Buisness_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buisness_Type
        fields = ['id', 'name']


class Buisness_sphereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buisness_Type
        fields = ['id', 'name']


class BranchEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchEmployee
        fields = ['branch', 'employee']

class BranchSerializer(serializers.ModelSerializer):
    employees = BranchEmployeeSerializer(many=True, read_only=True)  # Используйте EmployeeSerializer для вложенной сериализации сотрудников
    avatar = serializers.ImageField(required=False)  # Добавляем поле изображения
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())  # Добавляем поле проекта

    class Meta:
        model = Branch
        fields = ['id', 'country', 'city', 'address', 'name', 'active_days', 'work_hours', 'timeout', 'business', 'phone', 'user', 'project', 'avatar', 'employees']

    def create(self, validated_data):
        avatar = validated_data.pop('avatar', None)
        instance = super().create(validated_data)
        if avatar:
            instance.avatar = avatar
            instance.save()
        return instance

    

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'timezone', 'currency', 'colour', 'profile','id']