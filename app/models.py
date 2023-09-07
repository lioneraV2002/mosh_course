from django.db import models

# Create your models here.
# use model to collect data from the database and present to users


from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import UserManager

# When creating a custom user model AbstractBaseUser, you must provide fields is_staff and is_active

# to specify that the email field is used for user identification
# Set USERNAME_FIELD to 'email'.

#  you can define other fields that need to be filled out when creating a user by setting REQUIRED_FIELDS

# Finally, Set the objects attribute to the custom manager we created.




class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=20)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


    objects = UserManager()
    
    def __str__(self) -> str:
        return self.email