from django.shortcuts import render
from products.models import OrderProduct

from django.shortcuts import render
from products.models import OrderProduct

def view_bag(request):
    if request.user.is_authenticated:
        # Récupérer les OrderProduct via l'ordre lié à l'utilisateur
        order_products = OrderProduct.objects.filter(order__user=request.user)
        grand_total = sum(item.total_price() for item in order_products)
    else:
        order_products = []
        grand_total = 0

    return render(request, 'bag/view_bag.html', {
        'order_products': order_products,
        'grand_total': grand_total,
    })