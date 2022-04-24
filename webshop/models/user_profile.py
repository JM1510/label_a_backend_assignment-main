from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from rest_framework import permissions


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    
    def create_user(self,email,first_name,last_name,address,phone,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email,first_name=first_name,last_name=last_name,address=address,phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self,email,first_name,last_name,address,phone,password):
        """Create and save a new admin"""
        user = self.create_user(email,first_name,last_name,address,phone,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user
    

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """"Database model for auto company's users"""
    email = models.EmailField(max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    is_staff = models.BooleanField(default=False)
      
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    
    def get_address(self):
        """"Retrieve the user's address"""
        return f'{self.address}'
    
    def __str__(self):
        """"Return string representation of the user"""
        return self.email