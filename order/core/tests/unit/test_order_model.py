from django.test import TestCase

from order.core.models import Client, Order, OrderItem, Product


class OrderModelTestCase(TestCase):
    def test_should_has_attributes(self):
        self.assertIs(hasattr(Order, "client"), True)
        self.assertIs(hasattr(Order, "items"), True)
        self.assertIs(hasattr(Order, "created_at"), True)
        self.assertIs(hasattr(Order, "updated_at"), True)

    def test_str_model_object(self):
        client = Client(name="Luis")
        order = Order(client=client)
        expected = f"{order.id} - {order.client}"
        self.assertEqual(expected, str(order))


class OrderItemsModelTestCase(TestCase):
    def test_should_has_attributes(self):
        self.assertIs(hasattr(OrderItem, "item"), True)
        self.assertIs(hasattr(OrderItem, "order"), True)
        self.assertIs(hasattr(OrderItem, "quantity"), True)
        self.assertIs(hasattr(OrderItem, "unit_price"), True)

    def test_str_model_object(self):
        item = Product(
            name="Notebook", currency=Product.CurrencyChoices.REAL, price=2_599.00
        )
        order_item = OrderItem(item=item, quantity=10)
        expected = f"{order_item.quantity} x {order_item.item}"
        self.assertEqual(expected, str(order_item))
