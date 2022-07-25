from django.urls import path
from clientes import views

urlpatterns = [
    
    path('', views.clientes, name='Clientes'),
    path('formclientes/', views.formclientes, name='Formclientes'),
    path('busqueda/', views.busqueda, name='Buscar'),
    path('eliminar/<cliente_nombre>', views.eliminar, name='Eliminar'),
    path('editarcliente/<cliente_nombre>', views.edicioncliente, name='Editar'),

]