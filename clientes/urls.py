from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),

    path('crud', views.crud, name="crud"),
    path('clientesAdd', views.clientesAdd, name="clientesAdd"),
    path('clientes_del/<str:pk>', views.clientes_del, name='clientes_del'),
    path('clientes_findEdit/<str:pk>', views.clientes_findEdit, name='clientes_findEdit'),
    path('clientesUpdate', views.clientesUpdate, name='clientesUpdate'),

    path('crud_generos', views.crud_generos, name="crud_generos"),
    path('generosAdd', views.generosAdd, name="generosAdd"),
    path('generos_del/<str:pk>', views.generos_del, name="generos_del"),
    path('generos_edit/<str:pk>', views.generos_edit, name="generos_edit"),
]
