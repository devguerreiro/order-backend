from django.test import TestCase

from order.core.models import User


class UserModelTestCase(TestCase):
    def test_should_has_attributes(self):
        self.assertIs(hasattr(User, "username"), True)
        self.assertIs(hasattr(User, "email"), True)
        self.assertIs(hasattr(User, "password"), True)

    def test_str_model_object(self):
        user = User(email="devcorujam@gmail.com")
        self.assertEqual(user.email, str(user))
