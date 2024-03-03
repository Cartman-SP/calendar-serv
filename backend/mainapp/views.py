from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from mainapp.models import *
import json
from django.db.models import Q
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST , require_GET
import json
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model
from django.http import HttpResponseBadRequest
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usluga
from .serializers import *
import json
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Usluga
from .serializers import UslugaSerializer
import random
from rest_framework import status
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import get_object_or_404
from django.utils import timezone



@csrf_exempt
@require_POST
def register_user(request):
    try:
        data = json.loads(request.body)
        phone = data.get('phone', '')
        password = data.get('password', '')
        email = data.get('email', '')
        
        # Удаляем лишние символы из номера телефона
        phone = phone.replace('(', '').replace(')', '').replace(' ', '').replace('+', '').replace('-','')
        
        # Проверяем существует ли пользователь с таким телефоном
        if User.objects.filter(username=phone).exists():
            return JsonResponse({'error': 'Данный телефон уже используется'}, status=400)

        # Проверяем существует ли пользователь с такой почтой
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Пользователь с такой почтой уже существует'}, status=400)

        # Создаем нового пользователя
        user = User.objects.create_user(username=phone, password=password, email=email)

        # Вход пользователя после успешной регистрации
        auth_user = authenticate(request, username=phone, password=password)
        login(request, auth_user)

        # Возвращаем данные пользователя
        return JsonResponse({
            'user_id': user.id,
            'email': user.email,
            'phone': phone
        }, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

    
@csrf_exempt
@require_POST
def update_profile(request):
    name = request.POST.get('name', '')
    company_name = request.POST.get('company', '')
    timezoner = request.POST.get('timezone', '')
    currency = request.POST.get('currency', '')
    print(request.POST)
    user_id = request.POST.get('id', '')

    avatar = request.FILES.get('avatar', None)

    try:
        user = User.objects.get(id=user_id)
        profile, created = Profile.objects.get_or_create(user=user)
        profile.name = name
        profile.company_name = company_name
        profile.timezone = timezone
        profile.currency = currency
        profile.password_changed_at = timezone.now()
        if avatar:
            profile.avatar = avatar

        profile.save()

        return JsonResponse({'message': 'Профиль успешно обновлен'}, status=200)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Пользователь не найден'}, status=400)


@csrf_exempt
@require_POST
def get_profile(request):
    try:
        user_id = json.loads(request.body)['user_id']
        print(user_id)
        # Получаем пользователя и его профиль по ID
        user = User.objects.get(id=user_id)
        profile = Profile.objects.get(user=user)
        # Формируем данные о пользователе
        user_data = {
            'id': user.id,
            'phone': user.username,
            'email': user.email,
            'password_set': (profile.password_changed_at - timezone.now()).seconds//86400,
            'profile': {
                'name': profile.name,
                'company_name': profile.company_name,
                'timezone': profile.timezone,
                'currency': profile.currency,
                'avatar': profile.avatar.url
            }
        }

        return JsonResponse(user_data, status=200)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Пользователь не найден'}, status=404)
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'Профиль пользователя не найден'}, status=404)

@csrf_exempt
@require_POST
def login_user(request):
    try:
        data = json.loads(request.body)
        username_or_email = data.get('username_or_email')
        password = data.get('password')

        # Используем Q-объект для поиска пользователя по username или email
        user = User.objects.filter(Q(username=username_or_email) | Q(email=username_or_email)).first()

        # Попытка аутентификации пользователя
        user = authenticate(request, username=user.username, password=password)
        
        if user is not None:
            login(request, user)
            # Возвращаем данные пользователя, которые могут быть сохранены в Vuex
            return JsonResponse({
                'user_id': user.id,
                'email': user.email,
                'phone': user.username  # Допустим, что номер телефона хранится в поле username
            })
        else:
            return JsonResponse({'error': 'Неверный логин или пароль'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_POST
def check_profile(request, user_id):
    try:
        # Проверка существования пользователя
        user = User.objects.get(id=user_id)

        # Проверка наличия профиля
        try:
            profile = Profile.objects.get(user=user)
            print(123)
            return JsonResponse({'result': 1}, status=200)
        except Profile.DoesNotExist:
            # Если профиль не существует, возвращаем 0
            return JsonResponse({'result': 0}, status=200)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Пользователь не найден'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)



class UslugaList(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        user_id = request.GET.get('variable')
        uslugi = Usluga.objects.filter(user = User.objects.get(id=user_id))
        serializer = UslugaSerializer(uslugi, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        user = User.objects.get(id=request.data['user'])
        profile = Profile.objects.get(user=user)
        serializer = UslugaSerializer(data=request.data)
        if(profile.first_usluga==False):
            if serializer.is_valid():
                serializer.save()
                profile.first_usluga = True
                profile.save()
                return Response(True, status=201)
        if serializer.is_valid():
            serializer.save()
            return Response(False, status=201)
        return Response(serializer.errors, status=400)
    
@csrf_exempt    
def path_reset(request):
    data = json.loads(request.body.decode('utf-8'))
    email = data['email']
    print(111111111111111111111111111111111111111)
    user = User.objects.get(email=email)
    code = random.randint(1000,10000)
    a = Reset_passwrod(user = user,token=code)
    a.save()
    send_mail(
        'Востановление пароля',
        f'Ваш код востановления {code} \nНа сайте https://j0bar.ru/',
        'Daniil.shirkin005@yandex.ru',
        [email],
        fail_silently=False
    )
    return JsonResponse({'successes': "Письмо отправленно"})

@csrf_exempt
def change_pass(request):
    data = json.loads(request.body.decode('utf-8'))
    email = data['email']
    code = data['code']
    new_pass = data['password']
    print(email,code)
    user = User.objects.get(email=email)

    codes = Reset_passwrod.objects.filter(user=user).last()
    print(code)
    if codes.token == code:
        user.set_password(new_pass)
        user.save()
        prof = Profile.objects.get(user=user)
        prof.password_changed_at = timezone.now()
        response_data = {'is_valid': True}
        return JsonResponse(response_data, status=200)
    else:
        # If codes.token doesn't match the provided code or codes is not found, return a negative response
        response_data = {'is_valid': False}
        return JsonResponse(response_data, status=400)


@csrf_exempt
def change_pass_two(request):
    data = json.loads(request.body.decode('utf-8'))
    old_pass = data['old_pass']
    new_pass = data['new_pass']
    user_id = data['user_id']
    print(old_pass,new_pass,user_id)
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    if not check_password(old_pass, user.password):
        return JsonResponse({'error': 'Incorrect old password'}, status=400)

    # Change password
    user.set_password(new_pass)
    user.save()

    return JsonResponse({'message': 'Password changed successfully'})

@csrf_exempt
def usluga_delete(request):
    if request.method == 'POST':
        usluga_id = request.POST.get('id')  # Получаем идентификатор услуги из тела запроса
        print(usluga_id)
        try:
            usluga = Usluga.objects.get(id=usluga_id)  # Получаем объект услуги по идентификатору
            usluga.delete()  # Удаляем услугу
            return JsonResponse({'message': 'Услуга успешно удалена'})
        except Usluga.DoesNotExist:
            return JsonResponse({'error': 'Услуга с указанным идентификатором не найдена'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'Произошла ошибка при удалении услуги: {str(e)}'}, status=500)
    else:
        return JsonResponse({'error': 'Метод не разрешен'}, status=405)
    
@api_view(['POST'])
def create_employee(request):
    if request.method == 'POST':
        print(request.data )
        user_id = request.data.get('user_id')  # Получаем id пользователя из запроса
        try:
            user = User.objects.get(id=user_id)  # Получаем объект пользователя по id
            request.data['user'] = user.id  # Заменяем id пользователя на объект пользователя в данных запроса
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_employees_by_user(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')  # Получаем user_id из запроса
        employees = Employee.objects.filter(user_id=user_id)  # Получаем объекты Employee по user_id
        serializer = EmployeeSerializer(employees, many=True)
        print(serializer.data)
        return Response(serializer.data)
    
def get_usluga_name(request):
    if request.method == 'GET':
        try:
            usluga_id = request.GET.get('usluga_id').split(',')[:-1:]
            usluga_name=[]
            for i in usluga_id:
                usluga = Usluga.objects.get(id=i)
                usluga_name.append(usluga.name) 
            return JsonResponse({'usluga_name': usluga_name})
        except Usluga.DoesNotExist:
            return JsonResponse({'error': 'Usluga does not exist'}, status=404)


@csrf_exempt
@require_POST
def get_workers(request):
    user_id = json.loads(request.body)['user_id']
    user = User.objects.get(id=user_id)
    employees = Employee.objects.filter(user=user)

    serializer = EmployeeSerializer(employees, many=True)
    
    return JsonResponse(serializer.data, safe=False, status=200)

@api_view(['GET'])
def get_buisnessTypes(request):
    if request.method == 'GET':
        types = Buisness_Type.objects.all()
        serializer = Buisness_typeSerializer(types, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def get_buisnessSphere(request):
    if request.method == 'GET':
        types = Buisness_sphere.objects.all()
        serializer = Buisness_sphereSerializer(types, many=True)
        return Response(serializer.data)
    


@csrf_exempt
def create_branch(request):
    if request.method == 'POST':
        data = request.POST
        # Создание филиала
        branch = Branch.objects.create(
            country=data.get('country'),
            city=data.get('city'),
            address=data.get('address'),
            name=data.get('name'),
            active_days=data.get('active_days'),
            work_hours=data.get('work_hours'),
            timeout=data.get('timeout'),
            business=data.get('business'),
            user = User.objects.get(id = data.get('user_id')),
            phone = data.get('phone'),
        )
        
        # Обработка сотрудников
        employees_ids = data.getlist('choices[]')
        for employee_id in employees_ids:
            employee = Employee.objects.get(id=employee_id)
            BranchEmployee.objects.create(branch=branch, employee=employee)
        
        # Обработка выбранных типов бизнеса
        choices_ids = data.getlist('chips[]')
        for choice_id in choices_ids:
            choice = Buisness_Type.objects.get(id=choice_id)
            BranchType.objects.create(branch=branch, type=choice)
        
        # Обработка изображений
        images = request.FILES.getlist('images[]')
        print(images)
        for img in images:
            Image.objects.create(branch=branch, image=img)
        
        return JsonResponse({'message': 'Branch created successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


@api_view(['GET'])
def get_Branch(request):
    if request.method == 'GET':
        user_id = request.GET.get('variable')
        print(request.GET)
        branches = Branch.objects.filter(user=user_id)
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def get_image(request):
    if request.method == 'GET':
        branch_id = request.GET.get('id')
        print(branch_id)
        images = Image.objects.filter(branch=branch_id)
        
        # Retrieve the first object
        first_image = images.first()

        # Check if there's any image retrieved
        if first_image is not None:
            serializer = ImageSerializer(first_image)  # Serialize the first object
            return Response(serializer.data)  # Return serialized data in the response
        else:
            return Response(status=404)  # Return 404 if no image found
        
@csrf_exempt
def branch_delete(request):
    if request.method == 'POST':
        branch_id = request.POST.get('id')  # Получаем идентификатор услуги из тела запроса
        try:
            branch = Branch.objects.get(id=branch_id)  # Получаем объект услуги по идентификатору
            branch.delete()  
            return JsonResponse({'message': 'Услуга успешно удалена'})
        except Usluga.DoesNotExist:
            return JsonResponse({'error': 'Услуга с указанным идентификатором не найдена'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'Произошла ошибка при удалении услуги: {str(e)}'}, status=500)
    else:
        return JsonResponse({'error': 'Метод не разрешен'}, status=405)
    
@csrf_exempt
def update_name(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('id')
        new_name = data.get('name')

        if user_id is None or new_name is None:
            return JsonResponse({'error': 'Missing user_id or name'}, status=400)

        profile = Profile.objects.filter(user_id=user_id).first()

        if profile is None:
            return JsonResponse({'error': 'Profile not found'}, status=404)

        profile.name = new_name
        profile.save()

        return JsonResponse({'message': 'Name updated successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def update_avatar(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')

        if 'avatar' not in request.FILES:
            return JsonResponse({'error': 'No avatar provided'}, status=400)

        profile = Profile.objects.filter(user_id=user_id).first()

        if profile is None:
            return JsonResponse({'error': 'Profile not found'}, status=404)

        profile.avatar = request.FILES['avatar']
        profile.save()

        return JsonResponse({'message': 'Avatar updated successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)