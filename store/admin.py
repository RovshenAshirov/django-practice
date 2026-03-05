from django.contrib import admin

from store.models import Collection, Product, Customer, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']

    def collection_title(self, obj):
        return obj.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, obj):
        if obj.inventory < 10:
            return "Low"
        return "OK"


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ('first_name', 'last_name')
    list_per_page = 10


admin.site.register(Collection)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']
