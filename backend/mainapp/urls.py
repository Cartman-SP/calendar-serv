from django.urls import path
from mainapp.views import *
urlpatterns = [
    path('reg/', register_user, name='endpoint1'),
    path('login/', login_user, name='endpoint1'),
    path('password_reset/', custom_password_reset, name = 'create_link'),
]