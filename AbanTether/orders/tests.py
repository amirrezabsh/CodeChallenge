# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Order
from users.models import CustomUser

class PlaceOrderViewTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        self.user.balance = 20 # Initializing user with enough balance to pass successful order placement test
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_successful_order_placement(self):
        response = self.client.post('/api/orders/place_order/', {'currency': 'ABAN', 'amount': 5})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)

    def test_insufficient_balance(self):
        response = self.client.post('/api/orders/place_order/', {'currency': 'ABAN', 'amount': 1000})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Insufficient balance')
        self.assertEqual(Order.objects.count(), 0)

    def test_invalid_currency(self):
        response = self.client.post('/api/orders/place_order/', {'currency': 'INVALID', 'amount': 5})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('currency', response.data['error'])


    def test_error_handling(self):
        # Simulate an error during order placement
        with self.assertRaises(Exception):
            response = self.client.post('/api/orders/place_order/', {'currency': 'ABAN', 'amount': 'ab'})


    def test_authentication_required(self):
        client = APIClient()
        response = client.post('/api/orders/place_order/', {'currency': 'ABAN', 'amount': 5})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


