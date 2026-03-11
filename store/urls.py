from django.urls import path

from store.views import (
    ProductListCreateView, ProductRetrieveUpdateDestroyView, CollectionListCreateView,
    CollectionRetrieveUpdateDestroyView
)

urlpatterns = [
    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view()),
    path('collections/', CollectionListCreateView.as_view()),
    path('collections/<int:pk>/', CollectionRetrieveUpdateDestroyView.as_view(), name='collection-detail'),
]
