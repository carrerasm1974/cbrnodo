from django.http import JsonResponse
from django.urls import reverse

def navbars_context(request):
    # Datos para el primer navbar
    first_nav_options = [
           {"link": "/operaciones_cbr", "name": "Operaciones"},
           {"link": "/configuracion", "name": "Configuración"},
           {"link": "/usuarios", "name": "Usuarios"},
    ]
    return {"navppal": first_nav_options}

