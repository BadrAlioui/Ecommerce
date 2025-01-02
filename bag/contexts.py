from products.models import OrderProduct

def bag_contents(request):
    """
    Context processor to calculate the grand total of the user's cart.
    """
    grand_total = 0

    # Vérifiez si l'utilisateur est connecté
    if request.user.is_authenticated:
        # Récupérer les produits liés aux commandes de l'utilisateur
        order_products = OrderProduct.objects.filter(order__user=request.user, order__ordered=False)
        grand_total = sum(item.total_price() for item in order_products)

    # Retourner le contexte global
    return {
        'grand_total': grand_total,
    }