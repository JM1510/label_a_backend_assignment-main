from django.contrib import admin
from .models import user_profile, product, shopping_cart, order, shipment

admin.site.register(user_profile.UserProfile)
admin.site.register(product.Product)
admin.site.register(shopping_cart.ShoppingCart)
admin.site.register(shopping_cart.CartItem)
admin.site.register(order.Order)
admin.site.register(order.OrderItem)
admin.site.register(shipment.Shipment)


