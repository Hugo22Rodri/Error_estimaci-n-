from django.urls import path
from . import views

app_name = 'calculo_errores'

urlpatterns = [
    path('', views.calcular_errores_view, name='calcular_errores'),
]