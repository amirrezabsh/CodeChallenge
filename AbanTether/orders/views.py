# orders/views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order, Customer
from django.db.models import Sum




def buy_from_exchange(order):
    # Simulating buying from exchange
    print(f"Bought {order.amount} {order.currency} from exchange.")

currencies_price = {
    "ABAN":4,
    "SHIBA": 3,
    "ETHERIUM": 9,
    "BITCOIN": 10,
    "DOGECOIN":5
}

@csrf_exempt
def place_order(request):
    john = Customer(name='John',balance=1000)
    john.save()
    if request.method == 'POST':
        data = request.POST
        currency = data.get('currency')
        amount = int(data.get('amount'))
        price = currencies_price.get(currency)

        customer_name = "John"  # Assuming a single customer for simplicity
        customer, status = Customer.objects.get_or_create(name=customer_name)

        order = Order.objects.create(customer=customer, currency=currency, amount=amount)

        total_amount = Order.objects.filter(customer=customer, currency=currency).aggregate(Sum('amount'))['amount__sum']
        

        if total_amount >= 10:
            orders_to_process = Order.objects.filter(customer=customer, currency=currency)
            for o in orders_to_process:
                buy_from_exchange(o)
                o.is_checkedout = True
                o.save()

        customer.balance -= order.amount * price  # Hard-coded price for simplicity
        customer.save()

        return JsonResponse({'message': 'Order placed successfully'})
    
    return JsonResponse({'message': 'Invalid request method'})

