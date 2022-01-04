from django.contrib import admin
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'product_type', 'price', 'publish_date', 'product_views']
    fields = ['title', 'photo', 'product_type', 'price', 'publish_date', 'product_views']


admin.site.register(Product, ProductAdmin)