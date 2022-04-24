from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class ProductManager(BaseUserManager):
    """Manager for products"""
    def create_product(self,name,description, price = 0.0):
        """Create a new product"""
        if not name:
            raise ValueError('Products must have a name')
        
        product = self.model(name=name,description=description,price=price)
        product.save(using=self._db)
        return product
    
class Product(models.Model):
    """Database model for auto company's products"""
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    description = models.TextField()
    
    objects = ProductManager()
    
    def __str__(self):
        """Return string representation of the product"""
        return self.name