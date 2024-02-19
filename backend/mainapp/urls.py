from django.urls import path
from mainapp.views import *
urlpatterns = [
    path('reg/', register_user, name='endpoint1'),
    path('login/', login_user, name='endpoint1'),
    path('checkprofile/<int:user_id>', check_profile, name="have_profile"),
    path('uslugi/', UslugaList.as_view(), name="create_usluga"),
    path('pass_reset/', path_reset, name='path_reset'),
    path('change_pass/',change_pass, name="check_code"),
    path('delete/', usluga_delete, name='usluga_delete'),
    path('profile/', update_profile, name='create_profile'),
    path('getprofile/',get_profile,name='get_profile'),
    path('employee/', create_employee, name='create_employee'),
    path('get_employees/',get_employees_by_user,name='get_employees'),
    path('get_usluga_name/',get_usluga_name,name="get_usluga_name")
]