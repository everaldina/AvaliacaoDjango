from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from taygra_app.models import Produtos

# Create your views here.

def home (request):
    produtos = Produtos.objects.all()
    context = {'produtos':produtos}
    return render(request, 'index.html', context)


def categoria (request,id_produto):
    produto = Produtos.objects.get(id=id_produto)                                   
    context = {'produto':produto}
    return render(request, 'produto.html', context)

def informacoes (request,id_produto):
    produto = Produtos.objects.get(id=id_produto)                                   
    context = {'produto':produto}
    return render(request, 'produto.html', context)

def contatos (request,id_produto):
    produto = Produtos.objects.get(id=id_produto)                                   
    context = {'produto':produto}
    return render(request, 'produto.html', context)
      
    