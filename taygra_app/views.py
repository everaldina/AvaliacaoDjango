from django.shortcuts import render
from taygra_app.models import Oferta, Categoria, Produto
from django.apps import apps

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
