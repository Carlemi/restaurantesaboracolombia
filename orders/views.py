from django.urls import reverse
from django.shortcuts import render, redirect
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.core.management import call_command
from django.db import transaction


@transaction.atomic
def reiniciar_indices():
    # Eliminar todos los registros usando Django ORM
    Order.objects.all().delete()
    
    # Llamar a flush para reiniciar los índices
    call_command('flush', interactive=False)

def order_create(request):
  cart = Cart(request)
  if request.method == 'POST':
    form = OrderCreateForm(request.POST)
    if form.is_valid():
      order = form.save()
      for item in cart:
        OrderItem.objects.create(order=order,
                                 product=item['product'],
                                 price=item['price'],
                                 quantity=item['quantity'])
      # clear the cart
      cart.clear()
      #esto se ejecuta de manera asíncron
      order_created.delay(order.id)
      # set the order in the session
      request.session['order_id'] = order.id
      # redirect for payment
      return redirect(reverse('payment:process'))
  else:
    form = OrderCreateForm()
  return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})

