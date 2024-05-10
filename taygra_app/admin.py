from django.contrib import admin
from taygra_app.models import Produto, Categoria, Tamanho, Cor, Comentario, Oferta, Usuario, CarrinhoUsuario

# Register your models here.
admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Tamanho)
admin.site.register(Cor)
admin.site.register(Comentario)
admin.site.register(Oferta)
admin.site.register(Usuario)
admin.site.register(CarrinhoUsuario)
