from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el admin de Django
    path('', views.index, name='index'),
    path('listadoSQL/', views.listadoSQL, name='listadoSQL'),
    path('clientesAdd/', views.clientesAdd, name='clientesAdd'),
    path('clientesDel/<pk>/', views.clientes_del, name='clientesDel'),
    path('clientesFindEdit/<pk>/', views.clientes_findEdit, name='clientesFindEdit'),
    path('clientesUpdate/', views.clientesUpdate, name='clientesUpdate'),
    path('crud_generos/', views.crud_generos, name='crudGeneros'),
    path('generosAdd/', views.generosAdd, name='generosAdd'),
]


