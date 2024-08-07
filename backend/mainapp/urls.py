from django.urls import path
from mainapp.views import *
urlpatterns = [
    path('reg/', register_user, name='endpoint1'),
    path('login/', login_user, name='endpoint1'),
    path('checkprofile/<int:user_id>', check_profile, name="have_profile"),
    path('uslugi/', uslugas, name="create_usluga"),
    path('pass_reset/', path_reset, name='path_reset'),
    path('change_pass/',change_pass, name="check_code"),
    path('delete/', usluga_delete, name='usluga_delete'),
    path('profile/', update_profile, name='create_profile'),
    path('getprofile/',get_profile,name='get_profile'),
    path('employee/', create_employee, name='create_employee'),
    path('get_employees/',get_employees_by_user,name='get_employees'),
    path('get_usluga_name/',get_usluga_name,name="get_usluga_name"),
    path('change_pass_two/', change_pass_two,name ="change_pass_two"),
    path('getworkers/', get_workers, name = "getworkers"),
    path('get_buisnessTypes/', get_buisnessTypes, name='gettypes'),
    path('get_buisnessSphere/', get_buisnessSphere, name='gettypes'),
    path('createbranch/',create_branch, name='create_branch'),
    path('get_branch/',get_Branch,name="get_branch"),
    path('get_image/',get_image,name='get_image'),
    path('delete_branch/', branch_delete, name='branch_delete'),
    path('change_name/', update_name , name='change_name'),
    path('change_avatar/',update_avatar, name='change_avatar'),
    path('create_project/', CreateProjectAPIView.as_view(), name='create_project'),
    path('deleteemployee/',employee_delete,name='deleteemployee'),
    path('widget_create/',create_widget,name='widget_create'),
    path('uslugi_fromfilials/', get_uslugi_fromfilials ,name='get_uslugi_fromfilials'),
    path('change_mail/',change_mail,name="change_mail"),
    path('get_filialbyid/',get_filial_by_id, name='get_filialbyid/'),
    path('getuslugi_by_specialist/',getuslugi_by_specialist,name='getuslugi_by_specialist'),
    path('getspecialist_by_usluga/',getspecialist_by_usluga,name='getspecialist_by_usluga'),
    path('get_widget/', get_widget, name = 'get_widget'),
    path('get_branch_bylink/', get_branch_bylink, name='get_branch_bylink'),
    path('create_client/',create_client),
    path('create_applications/',create_applications),
    path('get_applications/',get_applications),
    path('get_client/',get_client),
    path('get_integration/',get_integration),
    path('client/<int:client_id>/applications/', get_client_applications, name='client-applications'),
    path('applications/', get_all_applications, name='all-applications'),
    path('employee/<int:employee_id>/', get_employee_byId, name='get_employeeById'),
    path('usluga/<int:usluga_id>/', get_usluga_byId, name='get_uslugaById'),
    path('client/delete/', client_delete, name='client_delete'),
    path('get_request/',get_request),
    path('delete_request/',delete_request),
    path('set_status/',set_status),
    path('get_widgetid/',get_widgetid),
    path('get_busytime/',get_busytime),
    path('get_employeebyid/',get_employee_by_id),
    path('get_uslugabyid/',get_usluga_by_id),
    path('get_clientbyid/',get_client_by_id),
    path('delete_widget/',delete_widget),
    path('get_time/',get_time),
    
    path('get_employee_stats/' ,get_employee_stats, name='employee-stats'), #НОВЫЕ ПУТИ
    path('widget-loads/',get_widget_loads, name='widget-loads'), #НОВЫЕ ПУТИ
    path('application-counts/', get_application_counts, name='application-counts'), #НОВЫЕ ПУТИ
    path('earnings/', get_earnings, name='get_earnings'), #???????????????????????????????????????
    path('new-application-count/', get_new_application_count, name='new-application-count'), #НОВЫЕ ПУТИ
    path('usluga/<int:usluga_id>/edit/', edit_usluga, name='edit_usluga'), #НОВЫЕ ПУТИ
    path('employee/<int:employee_id>/edit/', edit_employee, name='edit_employee'), #НОВЫЕ ПУТИ
    path('branch/<int:branch_id>/edit/', edit_branch, name='edit_branch'), #НОВЫЕ ПУТИ
    path('widget/<int:widget_id>/edit/', edit_widget, name='edit_widget'), #НОВЫЕ ПУТИ
    path('create_application_from_widget/', create_application_from_widget, name='create_application_from_widget'),
    path('widget_load/', widget_load, name='widget_load'), #НОВЫЕ ПУТИ
    path('set_color/<int:application_id>/', set_color_application, name='set_color_application'), #НОВЫЕ ПУТИ
]