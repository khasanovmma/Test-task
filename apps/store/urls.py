from rest_framework.routers import DefaultRouter

from .api.views import ProductAPIView


router = DefaultRouter()
router.register("product", ProductAPIView)


urlpatterns = []

urlpatterns += router.urls
