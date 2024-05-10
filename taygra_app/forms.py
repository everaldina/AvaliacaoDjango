from taygra_app.models import Produto, Categoria, Tamanho, Cor, Comentario, Oferta, Usuario, CarrinhoUsuario
from django import forms
from django.forms.widgets import *
from django.contrib.auth.models import User 

class LoginForm (forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username','password']
        widgets = {'password': PasswordInput()}
    def __init__ (self, *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Login','class':'col form-control my-2 p-2'})
        self.fields['password'].widget.attrs.update({'placeholder':'Senha','class':'col form-control my-2 p-2'})

class UserForm (forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username','password','first_name','last_name','email']
        widgets = {'password': PasswordInput()}
    def __init__ (self, *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['username'].widget.attrs.update({'required':'True','placeholder':'Login','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['password'].widget.attrs.update({'required':'True','placeholder':'Senha','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['first_name'].widget.attrs.update({'required':'True','placeholder':'Nome','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['last_name'].widget.attrs.update({'required':'True','placeholder':'Sobrenome','class':'col form-control my-2 p-2','autocomplete':'new-password'})
        self.fields['email'].widget.attrs.update({'required':'True','placeholder':'Email','class':'col form-control my-2 p-2','autocomplete':'new-password'})

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['username','password','first_name','last_name','email', 'telefone', 'cpf']
        labels = {
            'username': "Nome de usuário",
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'cpf': 'CPF ou CNPJ',
            'email': 'Email',
            'password' : 'Senha',
            'telefone' : 'Telefone',
        }       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Usuário*', 'required': 'required'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sobrenome*', 'required': 'required'})
        self.fields['cpf'].widget.attrs.update({'class': 'form-control', 'placeholder': 'CPF ou CNPJ*', 'required': 'required'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email*', 'required': 'required'})    
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha*', 'required': 'required'})    
        self.fields['telefone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Telefone*', 'required': 'required'})    
       