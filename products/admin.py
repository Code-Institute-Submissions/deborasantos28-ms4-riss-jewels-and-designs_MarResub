from django.contrib import admin
from .models import Product, Category, ProductReview

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    '''A function that displays a list
    of product parameters in the
    admin interface'''

    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "rating",
        "image",
    )


class CategoryAdmin(admin.ModelAdmin):
    '''A function that displays the category
    names with a friendly name on the
    admin interface'''

    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview)
