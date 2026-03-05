from django.contrib import admin

from store.models import Collection, Product, Customer


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # https://docs.djangoproject.com/en/4.2/ref/contrib/admin/  # ModelAdmin Options
    list_display = ['title', 'unit_price']
    list_editable = ['unit_price']
    list_per_page = 10

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ('first_name', 'last_name')
    list_per_page = 10

admin.site.register(Collection)
# admin.site.register(Product, ProductAdmin)
