from django.shortcuts import render
from taygra_app.models import Oferta, Categoria, Produto
from django.apps import apps
from django.http import HttpResponseRedirect
from django.urls import reverse
from taygra_app.forms import return_form

# Create your views here.

def home(request):
    ofertas = []
    oferta_principal = None
    for oferta in Oferta.objects.all():
        if oferta.nome == "Promoção":
            oferta_principal = oferta
        else:
            ofertas.append(oferta)
    
    if oferta_principal is not None and len(ofertas) != 0:
        oferta_principal = ofertas[0]
    context = {
        'oferta_principal': oferta_principal,
        'ofertas': ofertas
    }
    
    return render(request, 'index.html', context)

def categorias(request, categoria_id):
    categorias = Categoria.objects.all()
    categoria = categorias.get(pk=categoria_id)
    
    context = {
        'categorias': categorias,
        'categoria_selecionada': categoria
    }
    
    return render(request, 'categorias.html', context)

def informacoes(request):
    return render(request, 'informacoes.html')

def contato(request):
    return render(request, 'contato.html')

def tabela_tamanho(request):
    return render(request, 'tabela_tamanho.html')


def produto(request, id_produto):
    produto = Produto.objects.get(pk=id_produto)
    
    context = {
        'produto': produto
    }
    
    return render(request, 'produto.html', context)


def cadastro(request):
    return HttpResponseRedirect(reverse('cadastro_form'))

def cadastro_form(request, nome_form):
    form_list = {
        'produto': {'nome': 'Produto', 'nome_plural': 'produtos'},
        'categoria': {'nome': 'Categoria', 'nome_plural': 'categorias'},
        'tamanho': {'nome': 'Tamanho', 'nome_plural': 'tamanhos'},
        'cor': {'nome': 'Cor', 'nome_plural': 'cores'},
        'comentario': {'nome': 'Comentario', 'nome_plural': 'comentarios'},
        'oferta': {'nome': 'Oferta', 'nome_plural': 'ofertas'},
        'carrinho_usuario': {'nome': 'Carrinho usuario', 'nome_plural': 'produto ao carrinho'},
        
    }
    if request.method == "POST":
        form = return_form(nome_form, request.POST)
        if form and form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('formulario_nivel_formacao'))
    else:
        form = return_form(nome_form)

    context = {
        'form': form,
        'lista_form': form_list,
    }

    return render(request, 'cadastro.html', context)

