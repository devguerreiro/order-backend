from django.test import TestCase
from rest_framework.serializers import CharField, DecimalField, IntegerField

from order.core.serializers import ProductListSerializer, ProductRetrieveSerializer


class ProductListSerializerTestCase(TestCase):
    def test_should_has_fields(self):
        fields = ProductListSerializer().get_fields()
        self.assertIs(isinstance(fields.get("id"), IntegerField), True)
        self.assertIs(isinstance(fields.get("name"), CharField), True)
        self.assertIs(isinstance(fields.get("currency"), CharField), True)
        self.assertIs(isinstance(fields.get("price"), DecimalField), True)
        self.assertIs(isinstance(fields.get("multiplier"), IntegerField), True)


class ProductRetrieveSerializerTestCase(TestCase):
    def test_should_has_fields(self):
        fields = ProductRetrieveSerializer().get_fields()
        self.assertIs(isinstance(fields.get("id"), IntegerField), True)
        self.assertIs(isinstance(fields.get("name"), CharField), True)
        self.assertIs(isinstance(fields.get("currency"), CharField), True)
        self.assertIs(isinstance(fields.get("price"), DecimalField), True)
        self.assertIs(isinstance(fields.get("multiplier"), IntegerField), True)
