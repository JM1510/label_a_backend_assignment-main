from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""
    
    def has_object_permission(self,request,view,obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
    
class EditProduct(permissions.BasePermission):
    """Allow only staff users to add new products"""
    
    def has_object_permission(self, request, view, obj):
        """Check if user trying to handle a product is part of the staff"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser == True or request.user.is_staff == True
            