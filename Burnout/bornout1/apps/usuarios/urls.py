from django.urls import path , include
from apps.usuarios.views import indexusu,usuario_view


urlpatterns = [
    path(r'', indexusu, name='index'),
    path(r'nuevo', usuario_view, name='usuario_crear'),
]
