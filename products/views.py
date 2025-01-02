from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Order, OrderProduct



# Create your views here.
def all_products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/all_products.html', context)

#code institute
def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

def product_info(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product':product}
    return render(request, 'products/product-info.html', context)

def store(request):
    return render(request, 'products/store.html')

def t_shirts_view(request):
    try:
        # Récupérer la catégorie 'shirts'
        t_shirt_category = Category.objects.get(name='shirts')
        
        # Récupérer tous les produits associés à cette catégorie
        products = Product.objects.filter(category=t_shirt_category)

        # Renvoyer les produits au template
        return render(request, 'products/t_shirts.html', {'category': t_shirt_category, 'products': products})
    except Category.DoesNotExist:
        # Si la catégorie n'existe pas, afficher un message d'erreur
        return render(request, 'products/t_shirts.html', {'error': "Category 'shirts' does not exist."})

def shoes_view(request):
    try:
        # Récupérer la catégorie 'shoes'
        shoes_category = Category.objects.get(name='shoes')
        
        # Récupérer tous les produits associés à cette catégorie
        products = Product.objects.filter(category=shoes_category)

        # Renvoyer les produits au template
        return render(request, 'products/shoes.html', {'category': shoes_category, 'products': products})
    except Category.DoesNotExist:
        # Si la catégorie n'existe pas, afficher un message d'erreur
        return render(request, 'products/shoes.html', {'error': "Category 'shoes' does not exist."})