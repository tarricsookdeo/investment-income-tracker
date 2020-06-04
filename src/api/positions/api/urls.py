from rest_framework.routers import DefaultRouter

from .views import PositionViewSet

router = DefaultRouter()
router.register('', PositionViewSet, basename='position')
urlpatterns = router.urls
