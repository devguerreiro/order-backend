from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import GenericViewSet

from order.core.models import Product
from order.core.serializers import ProductListSerializer, ProductRetrieveSerializer


class ProductViewSet(GenericViewSet, ListAPIView, RetrieveAPIView):
    queryset = Product.objects.all()
    per_action_serializer = {
        "list": ProductListSerializer,
        "retrieve": ProductRetrieveSerializer,
    }

    def get_serializer_class(self):
        return self.per_action_serializer.get(self.action)
