from django.contrib import admin
from django.urls import path
from taygra_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produto/<id_produto>', views.produto, name='produto'),
    path('contato/', views.contato, name='contato'),
    path('informacao/', views.informacoes, name='informacoes'),
    path('tabela-tamanho/', views.tabela_tamanho, name='tabela-tamanho'),
    path('categorias/<id_categoria>', views.categorias, name='categorias'),
    path('categorias/<id_categoria>', views.categorias, name='categorias'),
    #path('form_produto/', views.form_produto, name ='form_produto'),
    #path('form_usuario/', views.form_usuario, name='form_usuario'),
    #path('login/', views.login, name='login')

]