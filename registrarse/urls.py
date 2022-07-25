from django.urls import path
from .views import RegistroUsuario, cierre_sesion, loguear

urlpatterns = [
    
    path('', RegistroUsuario.as_view(), name='Registro'),
    path('cierre_sesion', cierre_sesion, name='cierre_sesion'),
    path('loguear', loguear, name='Loguear'),

]