from django.urls import path
from . import views

app_name = 'programas'

urlpatterns = [
    path('programas/', views.programasv, name='lista_programas'),
]