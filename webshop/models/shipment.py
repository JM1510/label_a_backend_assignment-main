from xml.dom import ValidationErr
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .order import Order
from .user_profile import UserProfile

SHIPMENT_TIME = (
    ('Morning','8:00am - 12:00pm'),
    ('Afternoon','12:00pm - 5:00pm'),
    ('Evening','5:00pm - 8:00pm')
)

class Shipment(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    shipment_date = models.DateField()
    shipment_time = models.CharField(max_length=15,default='Morning',choices=SHIPMENT_TIME)
    
    
    def __str__(self):
        return f'{self.id}'

@receiver(post_save, sender=Shipment)
def ship_order(sender,instance,created,**kwargs):
    if created:
        item = Order.objects.get(pk=instance.order.id)
        item.status = "Pending Shipment"
        item.save()