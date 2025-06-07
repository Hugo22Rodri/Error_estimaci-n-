from django.urls import path
from . import views

app_name = 'estimacion_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('solve/', views.solve, name='solve'),
]