
from django.shortcuts import get_object_or_404, render

from base.models import CanalAnalogicoCarga, CanalAnalogicoEH

def config_canales(request):
    context = {
        'canales_cargas': list(CanalAnalogicoCarga.objects.all()),
        'navsec': [
           {"link": "/operaciones_cbr", "name": "Operaciones"},
           {"link": "/configuracion", "name": "Configuración"},
           {"link": "/usuarios", "name": "Usuarios"},
        ]
    }
    return render(request, 'configuracion/config_canales.html', context)
