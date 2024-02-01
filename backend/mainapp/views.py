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
from django.views.decorators.http import require_POST
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
import base64

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
def update_profile(request, user_id):
    try:
        data = json.loads(request.body)
        name = data['name']
        company_name = data['company_name']
        timezone = data['timezone']
        currency = data['currency']

        # Проверка существования пользователя
        user = User.objects.get(id=user_id)

        # Проверка наличия профиля
        profile, created = Profile.objects.get_or_create(user=user)

        # Обновление данных профиля
        profile.name = name
        profile.company_name = company_name
        profile.timezone = timezone
        profile.currency = currency
        profile.save()

        return JsonResponse({'message': 'Профиль успешно обновлен'}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


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
def custom_password_reset(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')

        # Check if a user with the specified email exists
        user = get_user_model().objects.get(email=email)

        # Generate a password reset token
        token = default_token_generator.make_token(user)

        # Create URL for resetting the password
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk)).decode()
        reset_url = f'http://127.0.0.1:8000/reset-password/{uidb64}/{urlsafe_base64_encode(force_bytes(token)).decode()}/'

        # Send email
        send_mail(
            'Password Reset',
            f'To reset your password, follow this link:\n\n{reset_url}',
            'Daniil.shirkin005@yandex.ru',
            [user.email],
            fail_silently=False,
        )

        return JsonResponse({'message': 'Password reset email sent successfully'})

    except get_user_model().DoesNotExist:
        return JsonResponse({'error': 'No user found with this email'}, status=400)

    except Exception as e:
        return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)

def reset_password_confirm(request, uidb64, token):
    try:
        # Decode UID and get the user
        uid = force_str(urlsafe_base64_decode(uidb64))
        user_model = get_user_model()
        user = user_model._default_manager.get(pk=uid)

        # Check the token
        if not default_token_generator.check_token(user, token):
            return HttpResponseBadRequest('Invalid reset link')

        if request.method == 'POST':
            # Process the form for setting a new password
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect('password_reset_complete')  # Replace with your target page after a successful password reset
        else:
            # Display the form for setting a new password
            form = SetPasswordForm(user)

        return render(request, 'reset_password_confirm.html', {'form': form, 'uidb64': uidb64, 'token': token})

    except (ValueError, OverflowError, user_model.DoesNotExist) as e:
        return HttpResponseBadRequest(f'Invalid reset link: {str(e)}')

    except Exception as e:
        return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)
    
def yaauth(request):
    context = {}
    print('123')
    context['token'] = 'token'
    return(request,'yareturn.html')