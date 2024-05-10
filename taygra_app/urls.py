from django.contrib import admin
from django.urls import path
from taygra_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produto/<id_produto>', views.produto, name='produto'),
    path('contato/', views.contato, name='contato'),
    path('informacoes/', views.informacoes, name='informacoes'),
    path('tabela-tamanho/', views.tabela_tamanho, name='tabela-tamanho'),
    path('categorias/<id_categoria>', views.categorias, name='categorias'),
    path('login/', views.login, name='login'),
    path('form_user/', views.form_user, name='form_user'),
    path('logout/', views.logout, name='logout'),
    path('newuser/', views.newuser, name='newuser'),
    path('deluser/<id>', views.deluser, name='deluser'),
    path('editperfil/', views.editperfil, name='editperfil'),
    path('categorias/<id_categoria>', views.categorias, name='categorias'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro/<nome_form>', views.cadastro_form, name='cadastro_form')

]