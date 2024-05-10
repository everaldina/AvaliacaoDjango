from django.shortcuts import render
from taygra_app.models import Oferta, Categoria, Produto
from django.apps import apps
from taygra_app.forms import LoginForm,UserForm, UsuarioForm
from django.http import HttpResponseRedirect, QueryDict
from django.urls import reverse
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User 


# Create your views here.

def index (request):
    context = {
                "produtos": Produto.objects.all(),
                'loginform' :  LoginForm(),
                'userform' : UserForm(),
            }
    if request.user.is_authenticated:
        context['userform'] = UserForm(instance=User.objects.get(id=request.user.id))
    
    return render(request,'index.html', context)

def login (request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user:
            auth_login(request, user = user)
    return HttpResponseRedirect(reverse('home'))

def logout (request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))

def newuser (request):
    if request.method == 'POST':
        user = UserForm(request.POST)
        print(user)
        if user.is_valid():
            print("valido")
            if user.data.get('password') != user.data.get('confirmacao'):
                user.add_error('password','A senha e confirmação devem ser iguais')
            else:
                user = user.save(commit=False)
                user.password = make_password(user.password)
                user.save()
                return HttpResponseRedirect(reverse('index'))
        context = {
                "produtos": Produto.objects.all(),
                'loginform' :  LoginForm(),
                'userform' : user,
        }
        return render(request,'index.html',context)
    return HttpResponseRedirect(reverse('index'))

def deluser (request, id):
    user = User.objects.get(id=id)
    user.delete()
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))

def editperfil (request):
    if request.method == 'POST':
        usuario = User.objects.get(id=request.user.id)
        novo_usuario = request.POST.copy()
        novo_usuario['password'] = usuario.password
        novo_usuario['username'] = usuario.username
        user = UserForm(instance=usuario, data=novo_usuario)
        if user.is_valid:
            user.save()
    return HttpResponseRedirect(reverse('index'))

def form_user(request):

    form = UsuarioForm()
   
    if request.method == 'POST':
        request_data = request.POST.copy()
        request_data['password'] = make_password(request_data['password'])
        form = UsuarioForm(request_data)
        if form.is_valid():
            form.save()
            form = UsuarioForm()
        return HttpResponseRedirect(reverse('home')) 

    context = {'form': form}    
    return render (request, 'form_user.html', context)

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
