from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('product/<slug:slug>/', views.product_info, name="product-info"),
    path('product/<product_id>', views.product_detail, name='product_detail'),
    path('store/', views.store, name='store'),
    path('t-shirts/', views.t_shirts_view, name='t_shirts'),
    path('shoes/', views.shoes_view, name='shoes'),
    
    
]