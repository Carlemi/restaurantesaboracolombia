from decimal import Decimal
from django.conf import settings
from shop.models import Product
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.sessions.models import Session
from django.apps import apps

order = apps.get_model('orders', 'Order')

class Cart:
    
    def __init__(self, request):
        """
        Iniciamos el carrito
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def __iter__(self):
        """
        Iteramos sobre los items del carrito y obtenemos los valores de la bd
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())


    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()


    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True


    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()


    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    

    @receiver(post_delete, sender=order)
    def limpiar_sesion_orden(sender, instance, **kwargs):
        # Limpiamos cualquier referencia a esta orden en las sesiones
        Session.objects.filter(
            session_data__contains=f"'orden_id': {instance.id}"
        ).delete()