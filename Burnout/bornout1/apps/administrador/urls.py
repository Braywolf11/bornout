from django.urls import path , include
from apps.administrador.views import indexad


urlpatterns = [
    path(r'', indexad),
]