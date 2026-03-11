from django.urls import path

from store.views import product_list, product_detail, collection_detail, collection_list

urlpatterns = [
    path('products/', product_list),
    path('products/<int:pk>/', product_detail),
    path('collections/', collection_list),
    path('collections/<int:pk>/', collection_detail, name='collection-detail'),
]
