from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

from store.views import ProductViewSet, CollectionViewSet, ReviewViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('collections', CollectionViewSet)

products_router = NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', ReviewViewSet, basename='reviews')

urlpatterns = router.urls + products_router.urls
