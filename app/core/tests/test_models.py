
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email(self):
     """Creating new user with email successfull"""
     email = "test@exigent-group.com"
     password = "test12345#"
     user  = get_user_model().objects.create_user(
              email=email,
              password=password
     )
     self.assertEqual(user.email, email)
     self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
     """Test new user email is normalized"""

     email = "test@EXIGENT-GROUP.com"
     user  = get_user_model().objects.create_user(
              email=email,
              password='test1234'
        )
     self.assertTrue(user.email,email.lower())

    def test_new_user_invalid_email(self):
     """Test user with no email raises error"""
     with self.assertRaises(ValueError):
          get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
     """Test creating a new superuser"""
     user = get_user_model().objects.create_superuser(
               'admin@exigent-group.com',
               'test123'
        )

     self.assertTrue(user.is_superuser)
     self.assertTrue(user.is_staff)





