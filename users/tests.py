from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='sam',
            email='sam@email.com',
            password='testpass123',
        )
        self.assertEqual(user.username, 'sam')
        self.assertEqual(user.email, 'sam@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
