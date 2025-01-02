from django.contrib import admin
from .models import Category, Product, Order, OrderProduct

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = [
        'name',
        'slug',
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = [
        'title', 
        'brand',
        'description',
        'slug',
        'rating',
        'image',
    ]

    ordering = ('title', )

admin.site.register(Order)

admin.site.register(OrderProduct)