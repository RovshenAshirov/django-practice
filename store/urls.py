from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from store.views import ProductViewSet, CollectionViewSet

# router = SimpleRouter()
# http://127.0.0.1:8000/store/
# http://127.0.0.1:8000/store/products.json
router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('collections', CollectionViewSet)

urlpatterns = router.urls
# urlpatterns = [
#     path('', include(router.urls)),
# ]
