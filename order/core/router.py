from rest_framework.routers import SimpleRouter

from order.core.views import ProductViewSet

router = SimpleRouter()
router.register("product", ProductViewSet, "product")
