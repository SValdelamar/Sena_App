from django.http import HttpResponse
from django.template import loader
from .models import Programa
# Create your views here.

def programasv(request):
    lista_programas = Programa.objects.all().order_by('nombre')
    template = loader.get_template('lista_programas')
    context = {
    'lista_programas': lista_programas,
    'total_programas': lista_programas.count(),
    }
    return HttpResponse(template.render(context, request))