from django.test import TestCase

from order.core.models import Product


class ProductModelTestCase(TestCase):
    def test_should_has_attributes(self):
        self.assertIs(hasattr(Product, "name"), True)
        self.assertIs(hasattr(Product, "currency"), True)
        self.assertIs(hasattr(Product, "price"), True)
        self.assertIs(hasattr(Product, "multiplier"), True)

    def test_str_model_object(self):
        product = Product(
            name="Notebook", currency=Product.CurrencyChoices.REAL, price=2_599_00
        )
        expected = f"{product.name} - {product.currency} {product.price}"
        self.assertEqual(expected, str(product))
