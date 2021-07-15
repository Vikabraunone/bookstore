from rest_framework import routers
from .views import BookViewSet
from .views import BookShopViewSet

router = routers.DefaultRouter()
router.register('api/bookshops', BookShopViewSet, 'bookshops')
router.register('api/books', BookViewSet, 'books')
urlpatterns = router.urls
