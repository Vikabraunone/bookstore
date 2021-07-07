from rest_framework import routers
from .api import BookViewSet
from .api import BookShopViewSet

router = routers.DefaultRouter()
router.register('api/bookshops', BookShopViewSet, 'bookshops')
router.register('api/books', BookViewSet, 'books')
urlpatterns = router.urls
