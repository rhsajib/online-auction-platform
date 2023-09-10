from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError(_("You must provide an email address."))
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()                         
        return user
    

    
    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff = True."))
        
        if other_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser = True."))
        
        return self.create_user(email, username, password, **other_fields)
    



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email        = models.EmailField(_('email address'), unique=True)
    username     = models.CharField(max_length=150, unique=True)
    first_name   = models.CharField(max_length=150, blank=True, null=True)
    last_name    = models.CharField(max_length=150, blank=True, null=True)
    mobile       = models.IntegerField(_('mobile number'), blank=True, null=True)
    about        = models.TextField(_('about'), max_length=500, blank=True, null=True)

    date_joined  = models.DateTimeField(auto_now_add=True)
    last_login   = models.DateTimeField(auto_now=True)

    is_staff     = models.BooleanField(default= False)
    is_superuser = models.BooleanField(default= False) 
    is_active    = models.BooleanField(default= True)

    
    USERNAME_FIELD =    'email'         # email wil be required for login
    REQUIRED_FIELDS = ['username'] 

    objects = CustomUserManager()


    class Meta:
        verbose_name_plural = "Custom Users"

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.username
