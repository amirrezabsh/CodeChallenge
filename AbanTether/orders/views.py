# orders/views.py
from .models import Order
from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ValidationError

# Hard-coded price for simplicity
currencies_price = {
    "ABAN":4,
    "SHIBA": 3,
    "ETHERIUM": 9,
    "BITCOIN": 10,
    "DOGECOIN":5
}

# This class is for placing orders process
class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def buy_from_exchange(self,amount, currency):
        # Simulating buying from exchange
        print(f"Bought {amount} {currency} with {amount * currencies_price.get(currency)}$ value from exchange.")

    def checkout(self, currency, price):

        checkout_threshold = 10
        # Filtering not checkedout orders
        total_not_checkedout_orders = Order.objects.filter(currency=currency, is_checkedout=False)
        total_amount = total_not_checkedout_orders.aggregate(Sum('amount'))['amount__sum']
        
        # Checking if the orders amount of money is above 10$
        if total_amount * price >= checkout_threshold:
            self.buy_from_exchange(total_amount, currency)
            total_not_checkedout_orders.update(is_checkedout=True)


    # Defining the POST method
    def post(self, request, *args, **kwargs):
        
        # Extracting data from the request
        data = request.data
        currency = data.get('currency')
        amount = int(data.get('amount'))
        user = request.user

        # Initializing the price of the specified currency
        price = currencies_price.get(currency)

        # Check if the user has sufficient balance
        if user.balance < amount * price:
            return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Inserting customer's order into the DB
            order = Order.objects.create(customer=user, currency=currency, amount=amount)

            # Processing customer's balance
            user.balance -= order.amount * price  
            user.save()

            # Checking if chekingout conditions are satisfied
            self.checkout(currency, price)

            return Response({'message': 'Order placed successfully'}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

