from .models import Produto
from .models import Categoria
from .models import Tamanho
from .models import Cor
from .models import Comentario
from .models import Oferta
from .models import Usuario
from .models import CarrinhoUsuario

from django import forms

def return_form(form_nome, conteudo = None):
    if form_nome == 'produto':
        return ProdutoForm(conteudo)
    elif form_nome == 'categoria':
        return CategoriaForm(conteudo)
    elif form_nome == 'tamanho':
        return TamanhoForm(conteudo)
    elif form_nome == 'cor':
        return CorForm(conteudo)
    elif form_nome == 'comentario':
        return ComentarioForm(conteudo)
    elif form_nome == 'oferta':
        return OfertaForm(conteudo)
    elif form_nome == 'carrinho_usuario':
        return CarrinhoUsuario(conteudo)
    else:
        return None

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'descricao', 'desconto', 'fk_categoria', 'fk_cor', 'fk_tamanho',
                  'detalhes', 'quantidade_vendida', 'quantidade_estoque', 'imagem_url']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['fk_categoria'].widget.attrs.update({'class': 'form-select', 'placeholder': 'Categoria*', 'required': 'required'})
        self.fields['fk_categoria'].empty_label = "Categoria*"
        
        self.fields['fk_cor'].widget.attrs.update({'class': 'form-select', 'placeholder': 'Cor'})
        self.fields['fk_cor'].empty_label = "Cor"
        
        self.fields['fk_tamanho'].widget.attrs.update({'class': 'form-select', 'placeholder': 'Tamanho'})
        self.fields['fk_tamanho'].empty_label = "Tamanho"
        
        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        self.fields['preco'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Preço*', 'required': 'required'})
        self.fields['desconto'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Desconto*', 'required': 'required'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descrição*', 'required': 'required'})
        self.fields['detalhes'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Detalhes*', 'required': 'required'})
        self.fields['quantidade_vendida'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Quantidade Vendida*', 'required': 'required'})
        self.fields['quantidade_estoque'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Quantidade Estoque*', 'required': 'required'})
        self.fields['imagem_url'].widget.attrs.update({'class': 'form-control', 'placeholder': 'URL da Imagem' })
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        
class TamanhoForm(forms.ModelForm):
    class Meta:
        model = Tamanho
        fields = ['valor']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['valor'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Valor*', 'required': 'required'})
        
class CorForm(forms.ModelForm):
    class Meta:
        model = Cor
        fields = ['nome']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'descricao', 'avaliacao', 'fk_produto']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['autor'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Autor*', 'required': 'required'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descrição*', 'required': 'required'})
        self.fields['avaliacao'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Avaliação*', 'required': 'required'})
        
        self.fields['fk_produto'].widget.attrs.update({'class': 'form-select', 'placeholder': 'Produto*', 'required': 'required'})
        self.fields['fk_produto'].empty_label = "Produto*"
        
class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['nome', 'produtos']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        
        self.fields['produtos'].widget.attrs.update({'class': 'form-select', 'placeholder': 'Produtos*', 'required': 'required'})
        self.fields['produtos'].empty_label = "Produtos*"
        
class CarrinhoUsuario(forms.ModelForm):
    class Meta:
        model = CarrinhoUsuario
        fields = ['fk_usuario', 'fk_produto', 'quantidade']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['fk_usuario'].widget.attrs.update({'class': 'form-select', 'placeholder': 'Usuário*', 'required': 'required'})
        self.fields['fk_usuario'].empty_label = "Usuário*"
        
        self.fields['fk_produto'].widget.attrs.update({'class': 'form-select', 'placeholder': 'Produto*', 'required': 'required'})
        self.fields['fk_produto'].empty_label = "Produto*"
        
        self.fields['quantidade'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Quantidade*', 'required': 'required'})
    
        
        
        


