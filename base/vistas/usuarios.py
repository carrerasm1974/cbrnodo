
from django.http import HttpResponse
from django.template import loader
from base.models import Usuario



def usuarios(request): 
    usuarios = Usuario.objects.all().values()
    template = loader.get_template('usuarios/usuarios.html')
    context = {
        'usuarios': usuarios,
    }
    return HttpResponse(template.render(context, request))

def usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    template = loader.get_template('usuario.html')
    context = {
        'usuario': usuario,
    }
    return HttpResponse(template.render(context, request))