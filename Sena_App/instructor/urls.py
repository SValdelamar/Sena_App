from django.urls import path
from . import views

app_name = 'instructor'

urlpatterns = [
    path('instructores/', views.instructores, name='lista_instructores'),
    ]