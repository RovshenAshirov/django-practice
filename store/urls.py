from django.urls import path

from store.views import collection_detail, ProductListCreateView, ProductDetail, CollectionListCreateView

urlpatterns = [
    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('collections/', CollectionListCreateView.as_view()),
    path('collections/<int:pk>/', collection_detail, name='collection-detail'),
]
