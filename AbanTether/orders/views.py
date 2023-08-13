from django.shortcuts import render

# Create your views here.
# orders/views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Customer, Order

def buy_from_exchange(order):
    # Simulating buying from exchange
    print(f"Bought {order.amount} {order.currency} from exchange.")

@csrf_exempt
def place_order(request):
    if request.method == 'POST':
        data = request.POST
        currency = data.get('currency')
        amount = float(data.get('amount'))

        customer_name = "John"  # Assuming a single customer for simplicity
        customer = get_object_or_404(Customer, name=customer_name)

        order = Order.objects.create(customer=customer, currency=currency, amount=amount)

        total_amount = Order.objects.filter(customer=customer, currency=currency).aggregate(models.Sum('amount'))['amount__sum']

        if total_amount >= 10:
            orders_to_process = Order.objects.filter(customer=customer, currency=currency)
            for o in orders_to_process:
                buy_from_exchange(o)
            orders_to_process.delete()

        customer.balance -= order.amount * 4  # Hard-coded price for simplicity
        customer.save()

        return JsonResponse({'message': 'Order placed successfully'})
    
    return JsonResponse({'message': 'Invalid request method'})
