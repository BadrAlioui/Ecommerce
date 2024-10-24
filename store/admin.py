from django.contrib import admin

#refer to https://www.udemy.com/course/python-django-build-an-e-commerce-store-2022/learn/lecture/34534700#overview
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)  
class ProductAdmin(admin.ModelAdmin):  
    prepopulated_fields = {'slug': ('title',)}
