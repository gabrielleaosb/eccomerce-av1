from django.shortcuts import render
from .models import Produto, Categoria, Plataforma, Sistema, Tipo, Distribuidor


def home(request):
    context = {
        'plataformas': Plataforma.objects.all(),
        'sistemas': Sistema.objects.all(),
        'tipos': Tipo.objects.all(),
        'categorias': Categoria.objects.all(),
        'distribuidores': Distribuidor.objects.all()
    }
    return render(request, 'loja/home.html', context)


def lista_produtos(request):
    produtos = Produto.objects.all()

    categoria_id = request.GET.get('categoria')
    if categoria_id:
        produtos = produtos.filter(categoria_id=categoria_id)
    
    return render(request, 'loja/produtos.html', {'produtos': produtos})
