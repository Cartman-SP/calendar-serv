from django.urls import path
from mainapp.views import *
urlpatterns = [
    path('yareg/', receive_data, name='endpoint1'),
    # Добавьте другие пути по мере необходимости
]