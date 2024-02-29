from django.contrib import admin

from liberty_market.models import Author, Item, Category, Order


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['item']
