from django.urls import include, path

from .vistas.usuarios import usuarios, usuario
from .vistas.edit_canal import edit_canal_carga, edit_canal_eh, edit_alarma_carga
from .vistas.config_canales import config_canales
from .vistas.operaciones_cbr import operaciones_cbr
from .vistas.home import signup, home, login

urlpatterns = [
    path("", home, name="inicio"),
    path("operaciones_cbr/", operaciones_cbr, name="operaciones_cbr" ),
    path('operaciones_cbr/details/<int:id>', operaciones_cbr, name="operaciones_cbr" ),
    path("usuarios/", usuarios, name="usuarios" ),
    path('usuarios/details/<int:id>', usuario, name='usuario'),
    path('modal_carga/<int:pk>/', edit_canal_carga.as_view(), name='edit_canal_carga'),
    path('modal_alarma_carga/<int:pk>/', edit_alarma_carga.as_view(), name='edit_alarma_carga'),
    path('modal_bobinas/<int:pk>/', edit_canal_eh.as_view(), name='edit_canal_eh'),
    path('configuracion/', config_canales, name='configuracion'),

    path("signup/", signup, name="signup" ),
    path("login/", login, name="login" ),

    path("accounts/", include("django.contrib.auth.urls")),

]