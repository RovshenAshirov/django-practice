from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

from store.views import ProductViewSet, CollectionViewSet, ReviewViewSet, CartViewSet, CartItemViewSet

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('collections', CollectionViewSet, basename='collections')
router.register('carts', CartViewSet, basename='carts')

products_router = NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', ReviewViewSet, basename='reviews')

carts_router = NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', CartItemViewSet, basename='items')

urlpatterns = router.urls + products_router.urls + carts_router.urls
