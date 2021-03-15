from django.test import TestCase

from order.core.models import User

class UserModelTestCase(TestCase):
    def test_should_has_attributes(self):
        self.assertIs(hasattr(User, "username"), True)
        self.assertIs(hasattr(User, "email"), True)
        self.assertIs(hasattr(User, "password"), True)
    
    def test_str_should_return_user_email(self):
        user = User(email="devcorujam@gmail.com")
        self.assertEqual(user.email, str(user))