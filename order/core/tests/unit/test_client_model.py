from django.test import TestCase

from order.core.models import Client

class ClientModelTestCase(TestCase):
    def test_should_has_attributes(self):
        self.assertIs(hasattr(Client, "name"), True)
    
    def test_str_should_return_client_name(self):
        client = Client(name="Luis")
        self.assertEqual(client.name, str(client))