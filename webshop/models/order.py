from django.db import models
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver
import decimal

from .shopping_cart import ShoppingCart, CartItem
from .product import Product

ORDER_STATUS = (
    ('Confirmed','Confirmed'),
    ('Pending shipment','Pending shipment'),
    ('Shipped','Shipped'),
)
class Order(models.Model):
    user = models.ForeignKey(ShoppingCart,on_delete=models.CASCADE)
    status = models.CharField(max_length=50,default='Confirmed',choices=ORDER_STATUS)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.id}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    subtotal = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)

    def __str__(self):
        return f'{self.id}'
    
@receiver(post_save, sender=Order)
def make_order(sender,instance,created,**kwargs):
    """When an order is created, the total price is calculated based on the items' current prices"""
    if created:
        total = decimal.Decimal(0.0)
        items = CartItem.objects.filter(user=instance.user)
        
        for item in items:
            product = Product.objects.get(id=item.product.id)
            quantity = item.quantity
            subtotal = product.price * quantity
            total += subtotal
            OrderItem.objects.create(order=instance,product=product,quantity=quantity,subtotal=subtotal)
        
        items.delete() # Remove items from shopping cart
        instance.total = total
        instance.save()