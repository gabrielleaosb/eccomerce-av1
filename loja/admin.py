from django.contrib import admin
from .models import Produto, Categoria, Plataforma, Sistema, Tipo, Distribuidor

admin.site.register(Produto)
admin.site.register(Plataforma)
admin.site.register(Sistema)
admin.site.register(Tipo)
admin.site.register(Categoria)
admin.site.register(Distribuidor)