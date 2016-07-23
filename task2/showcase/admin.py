from django.contrib import admin

from .models import Product, Tag


class ProductAdmin(admin.ModelAdmin):
    fields = ['title', 'rating', 'description', 'tags']


class TagAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Tag, TagAdmin)
