from django.contrib import admin
from parler.admin import TranslatableAdmin

from apps.models import Product


class ProductAdmin(TranslatableAdmin):
    pass


admin.site.register(Product, ProductAdmin)
