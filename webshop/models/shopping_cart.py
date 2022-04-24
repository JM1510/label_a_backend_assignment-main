from django.db import models
from django.db.models import F
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .user_profile import UserProfile
from .product import Product


class ShoppingCartManager(BaseUserManager):
    """Manager for shopping carts"""
    def create_shopping_cart(self,user,total=0.0):
        """Create a new shopping cart"""
        if not user:
            raise ValueError('Shopping carts must be tied to a user')
        
        cart = self.model(user=user,total=total)
        cart.save(using=self._db)
        
        return cart
    
    
class ShoppingCart(models.Model):
    """Database model for users' shopping carts"""
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    products = models.ManyToManyField(
        Product,
        related_name = 'carts',
        through = 'CartItem'
    )
    
    objects = ShoppingCartManager()
    
    def __str__(self):
        """Return string representation of the product"""
        return f'{self.id}'

class CartItemManager(BaseUserManager):
    """Manager for cart items"""
    def find_all_items(self,id,product):
        return self.filter(user=id,product=product)

class CartItem(models.Model):
    """Database model for items in a shopping cart"""
    user = models.ForeignKey(ShoppingCart,on_delete=models.CASCADE, related_name="cart_id")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
        
    def save(self,*args,**kwargs):
        """If the item is not in the shopping cart, add it. Otherwise, update quantity"""
        items = CartItem.objects.filter(user=self.user,product=self.product)
        if items:
            items.update(quantity=F('quantity') + self.quantity)
        else:
            return super(CartItem,self).save(*args,**kwargs)
        
    def __str__(self):
        """Return string representation of the product"""
        return f'{self.user} ({self.product} x{self.quantity})'

@receiver(post_save, sender=UserProfile)
def create_shopping_cart(sender, instance, created, **kwargs):
    """Automatically creates a shopping cart for each user created"""
    if created:
        ShoppingCart.objects.create(user=instance)




