from django.shortcuts import render
from products.models import OrderProduct

# Create your views here.
def view_bag(request):
    if request.user.is_authenticated:
        # Récupérer les articles du panier de l'utilisateur
        order_items = OrderProduct.objects.filter(user=request.user)
        # Calculer le grand total
        grand_total = sum(item.total_price() for item in order_items)
    else:
        order_items = []
        grand_total = 0

    return render(request, 'bag/bag.html', {
        'order_items': order_items,
        'grand_total': grand_total,
    })