from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from webshop import views


router = DefaultRouter()

router.register('profile',views.UserProfileViewSet)
router.register('product',views.ProductViewSet)
router.register('cart_item',views.CartItemViewSet,basename='cart_item')
router.register('order',views.OrderViewSet,basename='order')
router.register('order_item',views.OrderItemViewSet,basename='order_item')
router.register('shipment',views.ShipmentViewSet)

urlpatterns = [
    path('login/',views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]