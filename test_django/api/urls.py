from rest_framework.routers import DefaultRouter

from .views import ParsView

router = DefaultRouter()
router.register(r'items', ParsView, basename='user')

urlpatterns = router.urls


