from django.contrib.auth import authenticate, login
from django.utils.dateparse import parse_datetime
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
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import JsonResponse
import json
from django.utils import timezone
from django.utils import timezone
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Widget
from datetime import timedelta
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import timedelta
from .models import Employee, Application, Usluga
from django.utils import timezone
from datetime import timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Application
from django.utils import timezone
from datetime import timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Application
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Application
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Usluga, Employee, Branch, Widget
from .serializers import UslugaSerializer, EmployeeSerializer, BranchSerializer, WidgetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Client, Widget, Application
from .serializers import ClientSerializer, ApplicationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Client, Widget, Application
from .serializers import ClientSerializer, ApplicationSerializer
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from .models import WidgetLoad
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import Application


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
        profile = Profile.objects.create(user=user)
        profile.name = name
        profile.company_name = company_name
        profile.timezone = timezoner
        profile.currency = currency
        profile.password_changed_at = timezone.now()
        if avatar:
            profile.avatar = avatar

        profile.save()
        project, created = Project.objects.get_or_create(profile=profile)
        project.name = company_name
        project.timezone = timezoner
        project.currency = currency
        project.colour = "#F3F5F6"
        project.save()

        return JsonResponse({'message': 'Профиль успешно обновлен', 'project': project.id}, status=200)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Пользователь не найден'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


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



from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser

@csrf_exempt
@parser_classes([MultiPartParser, FormParser])
def uslugas(request):
    try:
        if request.method == 'GET':
            user_id = request.GET.get('variable')
            project = request.GET.get('project')
            print(project, '---------')
            uslugi = Usluga.objects.filter(user=User.objects.get(id=user_id), project=Project.objects.get(id=project))
            serializer = UslugaSerializer(uslugi, many=True)
            return JsonResponse(serializer.data, safe=False)  # Установите safe=False здесь
        elif request.method == 'POST':
            print(request.POST)
            user = User.objects.get(id=request.POST['user'])
            profile = Profile.objects.get(user=user)
            serializer = UslugaSerializer(data=request.POST)
            if not profile.first_usluga:
                if serializer.is_valid():
                    serializer.save()
                    profile.first_usluga = True
                    profile.save()
                    return JsonResponse(True, status=201, safe=False)  # Установите safe=False здесь
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(False, status=201, safe=False)  # Установите safe=False здесь
            return JsonResponse(serializer.errors, status=400, safe=False)  # Установите safe=False здесь
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500, safe=False)  # Установите safe=False здесь


    
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
    


def add_employee_to_service(string, employee_id):
    usluga_ids = string.split(',')
    usluga_ids = list(filter(bool, usluga_ids))
    for i in usluga_ids:
        usluga = Usluga.objects.get(id=i)
        usluga.employees = usluga.employees + ","+str(employee_id)
        usluga.save() 

@csrf_exempt
def create_employee(request):
    if request.method == 'POST':
        try:
            post_data = request.POST.dict()
            user_id = post_data.get('user_id')
            user = User.objects.get(id=user_id)
            post_data['user'] = user.id

            # Сериализуем данные расписания недели в формат JSON перед сохранением
            days = json.loads(post_data['daystime'])
            post_data['days'] = days

            serializer = EmployeeSerializer(data=post_data)
            profile = Profile.objects.get(user=user)

            if not profile.first_sotrudnik:
                if serializer.is_valid():
                    serializer.save()
                    profile.first_sotrudnik = True
                    profile.save()
                    add_employee_to_service(post_data.get('serviceid'), serializer.instance.id)
                    return JsonResponse(True, status=status.HTTP_201_CREATED, safe=False)
            elif serializer.is_valid():
                serializer.save()
                add_employee_to_service(post_data.get('serviceid'), serializer.instance.id)
                return JsonResponse(False, status=status.HTTP_201_CREATED, safe=False)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





@api_view(['GET'])
def get_employees_by_user(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id') 
        project = request.GET.get('project')
        employees = Employee.objects.filter(user_id=user_id,project = project)  # Получаем объекты Employee по user_id
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
    project_id = json.loads(request.body)['project']
    project = Project.objects.get(id=project_id)
    employees = Employee.objects.filter(user=user,project = project)

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
            project = Project.objects.get(id=data.get('project')),
            employees_id = data.get('employees'),
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
        profile = Profile.objects.get(user=User.objects.get(id = data.get('user_id')))
        if(profile.first_filial==False):
            profile.first_filial = True
            profile.save()
            return JsonResponse({'answer':True}, status=201)
        return JsonResponse({'answer':False}, status=201)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


@api_view(['GET'])
def get_Branch(request):
    if request.method == 'GET':
        user_id = request.GET.get('variable')
        project = request.GET.get('project')
        print(request.GET)
        branches = Branch.objects.filter(user=user_id,project=project)
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
    
class CreateProjectAPIView(APIView):
    def get(self, request):
        user_id = request.GET.get('user_id')
        if user_id is not None:
            try:
                user = User.objects.get(id=user_id)
                profile = user.profile
                projects = Project.objects.filter(profile=profile)

                # Создаем пустой словарь для хранения данных проектов с количеством услуг, филиалов и сотрудников
                project_data_list = []

                for project in projects:
                    # Получаем количество услуг, связанных с текущим проектом
                    num_services = Usluga.objects.filter(project=project).count()

                    # Получаем количество филиалов, связанных с текущим проектом
                    num_filials = Branch.objects.filter(project=project).count()

                    # Получаем количество сотрудников, связанных с текущим проектом
                    num_employees = Employee.objects.filter(project=project).count()

                    # Сериализуем текущий проект
                    serializer = ProjectSerializer(project)
                    project_data = serializer.data

                    # Добавляем количество услуг, филиалов и сотрудников к данным проекта
                    project_data['services'] = num_services
                    project_data['filials'] = num_filials
                    project_data['employees'] = num_employees

                    # Добавляем данные проекта в список
                    project_data_list.append(project_data)

                return Response(project_data_list)
            except User.DoesNotExist:
                return Response({'error': 'User with id {} does not exist'.format(user_id)}, status=status.HTTP_404_NOT_FOUND)
            except Profile.DoesNotExist:
                return Response({'error': 'Profile for user with id {} does not exist'.format(user_id)}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'user_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, *args, **kwargs):
        try:
            user_id = request.data.get('user_id')
            user = User.objects.get(id=user_id)
            profile = Profile.objects.get(user=user)
            request.data['profile'] = profile.id  # Добавляем ID профиля в данные запроса
            serializer = ProjectSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
def employee_delete(request):
    if request.method == 'POST':
        branch_id = request.POST.get('id')  # Получаем идентификатор услуги из тела запроса
        try:
            branch = Employee.objects.get(id=branch_id)  # Получаем объект услуги по идентификатору
            branch.delete()  
            return JsonResponse({'message': 'Услуга успешно удалена'})
        except Usluga.DoesNotExist:
            return JsonResponse({'error': 'Услуга с указанным идентификатором не найдена'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'Произошла ошибка при удалении услуги: {str(e)}'}, status=500)
    else:
        return JsonResponse({'error': 'Метод не разрешен'}, status=405)
    
@csrf_exempt
def create_widget(request):
    if request.method == 'POST':
        post_data = request.POST.dict()
        serializer = WidgetSerializer(data=post_data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)  # Печать ошибок сериализатора в консоль
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_uslugi_fromfilials(request):
    pass


@api_view(['POST'])
def change_mail(request):
    if request.method == 'POST':
        user_id = request.data.get('user_id')
        password = request.data.get('password')
        new_mail = request.data.get('new_mail')

        # Проверка наличия обязательных полей в запросе
        if not all([user_id, password, new_mail]):
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # Проверка аутентификации пользователя
        user = authenticate(request, username=user.username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_409_CONFLICT)

        # Проверка, что новый адрес электронной почты не привязан к другому пользователю
        try:
            existing_user_with_email = User.objects.get(email=new_mail)
            if existing_user_with_email != user:
                return Response({'error': 'Email already in use by another user'}, status=status.HTTP_409_CONFLICT)
        except User.DoesNotExist:
            pass  # Новый адрес электронной почты свободен

        # Изменение адреса электронной почты текущего пользователя
        user.email = new_mail
        user.save()

        return Response({'message': 'Email changed successfully'}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def get_filial_by_id(request):
    if request.method == 'GET':
        id = request.GET.get('variable')
        branch = Branch.objects.get(id=id)
        serializer = BranchSerializer(branch)
        return Response(serializer.data)
    
    
@api_view(['GET'])
def getuslugi_by_specialist(request):
    filial_id = int(request.GET.get('filial'))
    employee_id = int(request.GET.get('employee'))
    print(filial_id)
    if employee_id:
        employee = Employee.objects.get(id=employee_id)
        services_ids = employee.serviceid.split(',')
        services_ids = list(filter(bool, services_ids))
        services = Usluga.objects.filter(id__in=services_ids)
        serializer = UslugaSerializer(services, many=True)
        return Response(serializer.data)
    else:
        branch = Branch.objects.get(id=filial_id)
        employees_ids = branch.employees_id.split(',')
        employees_ids = list(filter(bool, employees_ids))
        employees = Employee.objects.filter(id__in=employees_ids)
        all_services = set()  # Множество для хранения уникальных услуг

        for employee in employees:
            services_ids = employee.serviceid.split(',')
            services_ids = list(filter(bool, services_ids))
            services = Usluga.objects.filter(id__in=services_ids)
            all_services.update(services)  # Добавляем услуги в множество

        serializer = UslugaSerializer(all_services, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getspecialist_by_usluga(request):
    filial_id = int(request.GET.get('filial'))
    usluga_id = int(request.GET.get('usluga'))
    if usluga_id:
        usluga = Usluga.objects.get(id=usluga_id)
        employees_ids = usluga.employees.split(',')
        employees_ids = list(filter(bool, employees_ids))
        employees = Employee.objects.filter(id__in=employees_ids)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    else:
        branch = Branch.objects.get(id=filial_id)
        employees_ids = branch.employees_id.split(',')
        employees_ids = list(filter(bool, employees_ids))
        employees = Employee.objects.filter(id__in=employees_ids)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def get_widget(request):
    if request.method == 'GET':
        user_id = request.GET.get('variable')
        project = request.GET.get('project')
        print(request.GET)
        branches = Widget.objects.filter(user=user_id,project=project)
        serializer = WidgetSerializer(branches, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def get_branch_bylink(request):
    if request.method == 'GET':
        company = request.GET.get('company')
        widget_name = request.GET.get('widget')
        profile = Profile.objects.get(company_name = company)
        user = profile.user
        widget = Widget.objects.get(user = user, name = widget_name)
        ids = widget.branches.split(',')
        branches = Branch.objects.filter(id__in=ids)
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)

@csrf_exempt
def create_client(request):
    if request.method == 'POST':
        serializer = ClientSerializer(data=request.POST)
        print(serializer)
        if serializer.is_valid():
            client = serializer.save()
            return JsonResponse({'client_id': client.id}, status=200, safe=False)  
        else:
            return JsonResponse({'error': 'invalid data'}, status=500, safe=False) 


@csrf_exempt
@parser_classes([MultiPartParser, FormParser])
def create_applications(request):
    try:
        if request.method == 'POST':
            serializer = ApplicationSerializer(data=request.POST)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(True, status=201, safe=False)  
            else:
                print("Serializer errors: ", serializer.errors)  # Добавлен вывод ошибок сериализатора
                return JsonResponse({'error': 'invalid data', 'details': serializer.errors}, status=500, safe=False) 
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500, safe=False) 


@api_view(['GET'])
def get_applications(request):
    if request.method == 'GET':
        project = request.GET.get('project')
        applications = Application.objects.filter(project=project)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def get_client(request):
    if request.method == 'GET':
        project = request.GET.get('project')
        clients = Client.objects.filter(project=project)
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_integration(request):
    if request.method == 'GET':
        integration = Integration.objects.filter()
        serializer = IntegrationSerializer(integration, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_client_applications(request, client_id):
    try:
        applications = Application.objects.filter(client_id=client_id)
        if not applications.exists():
            return Response(status=404, data={"message": "No applications found for this client"})
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response(status=500, data={"message": str(e)})

@api_view(['GET'])
def get_employee_byId(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    except Employee.DoesNotExist:
        return Response(status=404, data={"message": "Сотрудник не найден"})

@api_view(['GET'])
def get_usluga_byId(request, usluga_id):
    try:
        usluga = Usluga.objects.get(id=usluga_id)
        serializer = UslugaSerializer(usluga)
        return Response(serializer.data)
    except Usluga.DoesNotExist:
        return Response(status=404, data={"message": "Услуга не найдена"})


@csrf_exempt
def client_delete(request):
    if request.method == 'POST':
        client_id = request.POST.get('id')
        try:
            client = Client.objects.get(id=client_id)
            client.delete()
            return JsonResponse({'message': 'Клиент успешно удален'})
        except Client.DoesNotExist:
            return JsonResponse({'error': 'Клиент с указанным идентификатором не найден'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'Произошла ошибка при удалении клиента: {str(e)}'}, status=500)
    else:
        return JsonResponse({'error': 'Метод не разрешен'}, status=405)
    
@api_view(['GET'])
def get_all_applications(request, employee_id, filial_id):
    try:
        applications = Application.objects.filter(employee_id = employee_id)
        if not applications.exists():
            return Response(status=404, data={"message": "No applications found"})
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response(status=500, data={"message": str(e)})
    
@api_view(['GET'])
def get_request(request):
    if request.method == 'GET':
        filial = request.GET.get('filial')
        employee = request.GET.get('employee')
        applications = Application.objects.filter(branch=filial, employee=employee)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)


@csrf_exempt
def delete_request(request):
    if request.method == 'POST':
        request_id = request.POST.get('id')
        application = Application.objects.get(id=request_id)
        application.delete()
        return JsonResponse({'message': 'Клиент успешно удален'})
    
@csrf_exempt
def set_status(request):
    if request.method == 'POST':
        request_id = request.POST.get('id')
        application = Application.objects.get(id=request_id)
        application.status = request.POST.get('status')
        application.save()
        return JsonResponse({'message': 'Клиент успешно удален'})
    



@api_view(['GET'])
def get_widgetid(request):
    if request.method == 'GET':
        name = request.GET.get('widgetname')
        widget = Widget.objects.get(name=name)
        serializer = WidgetSerializer(widget)
        return Response(serializer.data)




@api_view(['GET'])
def get_busytime(request):
    if request.method == 'GET':
        employee_id = request.GET.get('employee_id')
        date_str = request.GET.get('date')  # предположим, что date приходит в формате 'YYYY-MM-DD'
        print(employee_id, date_str)
        
        # Фильтруем записи, где employee_id совпадает и дата в time совпадает с date_filter
        applications = Application.objects.filter(
            employee=employee_id, 
            data=date_str
        )
        print(applications)
        serializer = ApplicationTimeSerializer(applications, many=True)
        times = [entry['time'] for entry in serializer.data]
        return Response(times)


@api_view(['GET'])
def get_employee_by_id(request):
    if request.method == 'GET':
        id = request.GET.get('variable')
        employee = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

@api_view(['GET'])
def get_usluga_by_id(request):
    if request.method == 'GET':
        id = request.GET.get('variable')
        usluga = Usluga.objects.get(id=id)
        serializer = UslugaSerializer(usluga)
        return Response(serializer.data)

@api_view(['GET'])
def get_filial_by_id(request):
    if request.method == 'GET':
        id = request.GET.get('variable')
        branch = Branch.objects.get(id=id)
        serializer = BranchSerializer(branch)
        return Response(serializer.data)
    
@api_view(['GET'])
def get_client_by_id(request):
    if request.method == 'GET':
        id = request.GET.get('variable')
        client = Client.objects.get(id=id)
        serializer = ClientSerializer(client)
        return Response(serializer.data)
    
@csrf_exempt
def delete_widget(request):
    if request.method == 'POST':
        request_id = request.POST.get('id')
        widget = Widget.objects.get(id=request_id)
        widget.delete()
        return JsonResponse({'message': 'Виджет успешно удален'})
    
def parse_interval(interval_str): 
    parts = interval_str.split()
    hours = 0
    minutes = 0
    for i, part in enumerate(parts):
        if 'час' in part:
            hours = int(parts[i - 1])
        elif 'минут' in part:
            minutes = int(parts[i - 1])
    return timedelta(hours=hours, minutes=minutes)

def split_time(work_time, interval_str, break_time_str):
    interval = parse_interval(interval_str)
    break_start_str, break_end_str = break_time_str.split(' — ')
    break_start = datetime.strptime(break_start_str, '%H:%M')
    break_end = datetime.strptime(break_end_str, '%H:%M')

    start_time_str, end_time_str = work_time.split(' — ')
    start_time = datetime.strptime(start_time_str, '%H:%M')
    end_time = datetime.strptime(end_time_str, '%H:%M')
    
    result = {}
    current_time = start_time
    
    while current_time < end_time:
        next_time = current_time + interval
        if next_time > end_time:
            next_time = end_time
        if current_time < break_start or current_time >= break_end:
            result[current_time.strftime('%H:%M')] = True
        current_time = next_time
    
    return result

def check_time_in_interval(time, start_time_str, interval_str):
    start_time = datetime.strptime(start_time_str, '%H:%M').time()
    end_time = (datetime.strptime(start_time_str, '%H:%M') + parse_interval(interval_str)).time()
    
    return start_time <= time.time() <= end_time
@api_view(['GET'])
def get_time(request):  
    if request.method == 'GET':
        employee_id = request.GET.get('employee_id')
        dayofWeek = request.GET.get('dayofWeek')
        employee = Employee.objects.get(id=employee_id)
        usluga_id = request.GET.get('usluga_id')
        usluga = Usluga.objects.get(id = usluga_id)
        applications = Application.objects.filter(employee=employee)

        time = split_time(json.loads(employee.daystime)[dayofWeek]['work_time'], usluga.time,json.loads(employee.daystime)[dayofWeek]['chill_time'])
        for i in time.keys():
            for j in applications:
                if(check_time_in_interval(j.time,i,usluga.time)):
                    time[i] = False
                    break
        print(time)
        return Response(status=200, data=time)
@api_view(['GET'])
def get_employee_stats(request):
    if request.method == 'GET':
        employee_id = request.GET.get('employee_id')
        period = request.GET.get('period')  # day, week, month, quarter, year
        
        employee = get_object_or_404(Employee, id=employee_id)
        
        # Текущая дата и время
        now = timezone.now()
        
        if period == 'day':
            start_date = now - timedelta(days=1)
        elif period == 'week':
            start_date = now - timedelta(weeks=1)
        elif period == 'month':
            start_date = now - timedelta(days=30) 
        elif period == 'quarter':
            start_date = now - timedelta(days=90)  
        elif period == 'year':
            start_date = now - timedelta(days=365)
        else:
            return Response({'error': 'Invalid period specified'}, status=400)
        
        completed_statuses = ['Done'] #??????????????????????????????????????????????????????? 
        applications = Application.objects.filter(
            employee=employee, 
            time__gte=start_date, 
            time__lte=now, 
            status__in=completed_statuses
        )
        applications_count = applications.count()
        
        total_income = 0
        for application in applications:
            usluga = application.usluga
            total_income += float(usluga.cost)
        stats = {
        'employee': {
            'id': employee.id,
            'firstname': employee.firstname,
            'secondname': employee.secondname,
        },
        'applications_count': applications_count,
        'total_income': total_income
        }
        
        return Response(stats, status=200)
@api_view(['GET'])
def get_widget_loads(request):
    if request.method == 'GET':
        period = request.GET.get('period')  # today, yesterday, 7_days, 30_days
        project = request.GET.get('project')

        now = timezone.now()

        if period == 'today':
            start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
        elif period == 'yesterday':
            start_date = (now - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
            end_date = start_date + timedelta(days=1)
        elif period == '7_days':
            start_date = now - timedelta(days=7)
        elif period == '30_days':
            start_date = now - timedelta(days=30)
        else:
            return Response({'error': 'Invalid period specified'}, status=400)

        if period == 'yesterday':
            widget_loads = WidgetLoad.objects.filter(load_time__gte=start_date, load_time__lt=end_date, project=project)
        else:
            widget_loads = WidgetLoad.objects.filter(load_time__gte=start_date, load_time__lte=now, project=project)

        widget_load_count = widget_loads.count()

        return Response({'widget_load_count': widget_load_count}, status=200)
@api_view(['GET'])
def get_application_counts(request):
    if request.method == 'GET':
        period = request.GET.get('period')  # today, yesterday, 7_days, 30_days
        project = request.GET.get('project')
        
        now = timezone.now()

        if period == 'today':
        # Сегодня: с начала текущего дня до текущего момента
            start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
            end_date = now
        elif period == 'yesterday':
        # Вчера: с начала вчерашнего дня до начала сегодняшнего дня
            start_date = (now - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
            end_date = start_date + timedelta(days=1)
        elif period == '7_days':
        # Последние 7 дней: начиная с 7 дней назад до текущего момента
            start_date = now - timedelta(days=7)
            end_date = now
        elif period == '30_days':
        # Последние 30 дней: начиная с 30 дней назад до текущего момента
            start_date = now - timedelta(days=30)
            end_date = now

    # Фильтруем заявки по определенному периоду
        applications = Application.objects.filter(time__gte=start_date, time__lte=end_date, project=project)
    
    # Получаем количество отфильтрованных заявок
        applications_count = applications.count()

        return Response({'applications_count': applications_count}, status=200)

@api_view(['GET'])
def get_earnings(request):
    if request.method == 'GET':
        period = request.GET.get('period')  # today, yesterday, 7_days, 30_days
        project = request.GET.get('project')

        now = timezone.now()

        if period == 'today':
        # Сегодня: с начала текущего дня до текущего момента
            start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
            end_date = now
        elif period == 'yesterday':
        # Вчера: с начала вчерашнего дня до начала сегодняшнего дня
            start_date = (now - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
            end_date = start_date + timedelta(days=1)
        elif period == '7_days':
        # Последние 7 дней: начиная с 7 дней назад до текущего момента
            start_date = now - timedelta(days=7)
            end_date = now
        elif period == '30_days':
        # Последние 30 дней: начиная с 30 дней назад до текущего момента
            start_date = now - timedelta(days=30)
            end_date = now

    # Фильтруем заявки по определенному периоду
        applications = Application.objects.filter(time__gte=start_date, time__lte=end_date, project=project)

        total_earnings = 0
        for application in applications:
            usluga = application.usluga
            total_earnings += float(usluga.cost)

        return Response({'total_earnings': total_earnings}, status=200)

@api_view(['GET'])
def get_new_application_count(request):
    if request.method == 'GET':
        new_status = 'New' 
        new_applications_count = Application.objects.filter(status=new_status).count()
        
        return Response({'new_applications_count': new_applications_count}, status=200)

@api_view(['PATCH'])
def edit_usluga(request, usluga_id):
    usluga = get_object_or_404(Usluga, id=usluga_id)
    serializer = UslugaSerializer(usluga, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    serializer = EmployeeSerializer(employee, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def edit_branch(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    serializer = BranchSerializer(branch, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def edit_widget(request, widget_id):
    widget = get_object_or_404(Widget, id=widget_id)
    serializer = WidgetSerializer(widget, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_application_from_widget(request):
    application_data = request.data.get('application')
    
    # Создание заявки
    application_serializer = ApplicationSerializer(data=application_data)
    if application_serializer.is_valid():
        application = application_serializer.save()
        return Response(application_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(application_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def widget_load(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        widget_id = data.get('widget_id')
        load_time = data.get('load_time')
        project = data.get('project')

        try:
            widget = Widget.objects.get(id=widget_id)
        except Widget.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Widget not found'}, status=404)

        load_time = parse_datetime(load_time)

        if not load_time:
            return JsonResponse({'status': 'error', 'message': 'Invalid load_time format'}, status=400)

        WidgetLoad.objects.create(widget=widget, load_time=load_time, project_id=project)
        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'error'}, status=400)

@csrf_protect
def set_color_application(request, application_id):
    if request.method == 'POST':
        hex_color = request.POST.get('color')
        if not hex_color:
            return JsonResponse({'error': 'No color provided'}, status=400)

        try:
            application = Application.objects.get(id=application_id)
            application.color = hex_color
            application.save()
            return JsonResponse({'success': 'Color updated successfully'})
        except Application.DoesNotExist:
            return JsonResponse({'error': 'Application not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
def parse_interval(interval_str):
    parts = interval_str.split()
    hours = 0
    minutes = 0
    for i, part in enumerate(parts):
        if 'час' in part:
            hours = int(parts[i - 1])
        elif 'минут' in part:
            minutes = int(parts[i - 1])
    return timedelta(hours=hours, minutes=minutes)

def split_time(work_time, interval_str, break_time_str):
    interval = parse_interval(interval_str)
    break_start_str, break_end_str = break_time_str.split(' — ')
    break_start = datetime.strptime(break_start_str, '%H:%M')
    break_end = datetime.strptime(break_end_str, '%H:%M')

    start_time_str, end_time_str = work_time.split(' — ')
    start_time = datetime.strptime(start_time_str, '%H:%M')
    end_time = datetime.strptime(end_time_str, '%H:%M')
    
    result = {}
    current_time = start_time
    
    while current_time < end_time:
        next_time = current_time + interval
        if next_time > end_time:
            next_time = end_time
        if current_time < break_start or current_time >= break_end:
            result[current_time.strftime('%H:%M')] = True
        current_time = next_time
    
    return result

def check_time_in_interval(time, start_time_str, interval_str):
    start_time = datetime.strptime(start_time_str, '%H:%M').time()
    end_time = (datetime.strptime(start_time_str, '%H:%M') + parse_interval(interval_str)).time()
    
    return start_time <= time.time() <= end_time

@api_view(['GET'])
def get_time(request):
    if request.method == 'GET':
        employee_id = request.GET.get('employee_id')
        dayofWeek = request.GET.get('dayofWeek')
        date_str = request.GET.get('date')
        
        # Получаем дату из запроса
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        employee = get_object_or_404(Employee, id=employee_id)
        usluga_id = request.GET.get('usluga_id')
        usluga = get_object_or_404(Usluga, id=usluga_id)
        
        # Фильтруем заявки по сотруднику и дате
        applications = Application.objects.filter(employee=employee, time__date=date)
        print(applications)
        daystime = json.loads(employee.daystime)
        work_time = daystime[dayofWeek]['work_time']
        chill_time = daystime[dayofWeek]['chill_time']
        
        time = split_time(work_time, usluga.time, chill_time)
        
        for i in time.keys():
            for j in applications:
                if check_time_in_interval(j.time, i, usluga.time):
                    time[i] = False
                    break
        
        print(time)
        return Response(status=200, data=time)