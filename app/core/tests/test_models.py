from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successfully(self):
        """Test create user successfully"""
        email = 'testing123@gmail.com'
        password = 'Testing1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Normalize email test"""
        email='test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test1234')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """No email test"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '12345')

    
    def test_create_new_superuser(self):
        """Superuser test"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'testing123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)