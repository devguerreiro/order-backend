from rest_framework.serializers import CharField, DecimalField, IntegerField, Serializer


class ProductListSerializer(Serializer):
    id = IntegerField()
    name = CharField()
    currency = CharField()
    price = DecimalField(max_digits=9, decimal_places=2)
    multiplier = IntegerField()


class ProductRetrieveSerializer(ProductListSerializer):
    pass
