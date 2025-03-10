from django.shortcuts import render
from .models import Produto, Categoria

def home(request):
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'loja/home.html', {'produtos': produtos, 'categorias': categorias})

def lista_produtos(request):
    produtos = Produto.objects.all()

    categoria_id = request.GET.get('categoria')
    if categoria_id:
        produtos = produtos.filter(categoria_id=categoria_id)
    
    return render(request, 'loja/produtos.html', {'produtos': produtos})
