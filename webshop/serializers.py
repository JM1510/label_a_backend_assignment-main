from rest_framework import serializers

from .models import user_profile, product, shopping_cart, order, shipment

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    
    class Meta:
        model = user_profile.UserProfile
        fields = ('id','email','first_name','last_name','password')
        extra_kwargs = {
            'password' : {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
    
    def create(self,validated_data):
        """Create and return a new user"""
        user = user_profile.UserProfile.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
        )

        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance,validated_data)

class ProductSerializer(serializers.ModelSerializer):
    """Serializes a product object"""
    
    class Meta:
        model = product.Product
        fields = ('id','name','price','description')

class ShoppingCartSerializer(serializers.ModelSerializer):
    """Serializes a shopping cart object"""
    
    class Meta:
        model = shopping_cart.ShoppingCart
        fields = ('id','user')
    
class CartItemSerializer(serializers.ModelSerializer):
    """Serializes a new cart item object"""
    
    class Meta:
        model = shopping_cart.CartItem
        fields = ('id','user','product','quantity')
        
class OrderSerializer(serializers.ModelSerializer):
    """Serializes a new order object"""
    
    class Meta:
        model = order.Order
        fields = ('id','user','date','status','total')

class OrderItemSerializer(serializers.ModelSerializer):
    """Serializes a new order item object"""
    
    class Meta:
        model = order.OrderItem
        fields = ('id','order','product','quantity','subtotal')

class ShipmentSerializer(serializers.ModelSerializer):
    """Serializes the shipment of orders"""
    
    class Meta:
        model = shipment.Shipment
        fields = ('id','order','shipment_date','shipment_time')
