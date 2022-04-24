from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from webshop import serializers
from .models import user_profile, product, shopping_cart, order, shipment
from webshop import permissions

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = user_profile.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name','last_name','email',)
    
class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
class ProductViewSet(viewsets.ModelViewSet):
    """Handle creating and updating products"""
    serializer_class = serializers.ProductSerializer
    queryset = product.Product.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.EditProduct,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

class ShoppingCartViewSet(viewsets.ModelViewSet):
    """Handle creating shopping carts"""
    serializer_class = serializers.ShoppingCartSerializer
    queryset = shopping_cart.ShoppingCart.objects.all()

class CartItemViewSet(viewsets.ModelViewSet):
    """Handle items in a shopping cart"""
    serializer_class = serializers.CartItemSerializer
    
    def get_queryset(self):
        """Enables search of all items in a user's shopping cart"""
        queryset = shopping_cart.CartItem.objects.all()
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset

class OrderViewSet(viewsets.ModelViewSet):
    """Handle creating orders"""
    serializer_class = serializers.OrderSerializer
    
    def get_queryset(self):
        """Enables search of all of a user's orders"""
        queryset = order.Order.objects.all()
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset
    
class OrderItemViewSet(viewsets.ModelViewSet):
    """Handle items in an order"""
    serializer_class = serializers.OrderItemSerializer

    def get_queryset(self):
        """Enables search of all items in an order"""
        queryset = order.OrderItem.objects.all()
        order_number = self.request.query_params.get('order')
        if order_number is not None:
            queryset = queryset.filter(order=order_number)
        return queryset

class ShipmentViewSet(viewsets.ModelViewSet):
    """Handle creating shipments"""
    serializer_class = serializers.ShipmentSerializer
    queryset = shipment.Shipment.objects.all()


    
    
    