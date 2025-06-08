from django.urls import path
from . import views

app_name = 'calculo_errores'

urlpatterns = [
    path('', views.calcular_errores, name='calcular_errores'),
    path('resultados/', views.resultados, name='resultados'),
]