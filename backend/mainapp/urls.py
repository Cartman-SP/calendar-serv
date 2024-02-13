from django.urls import path
from mainapp.views import *
urlpatterns = [
    path('reg/', register_user, name='endpoint1'),
    path('login/', login_user, name='endpoint1'),
    path('password_reset/', custom_password_reset, name = 'create_link'),
    path('checkprofile/<int:user_id>', check_profile, name="have_profile"),
    path('uslugi/', UslugaList.as_view(), name="create_usluga")
]