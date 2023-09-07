from django.db import models

# Create your models here.
# use model to collect data from the database and present to users


from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import UserManager

# When creating a custom user model AbstractBaseUser, you must provide fields is_staff and is_active.
# to specify that the email field is used for user identification
# Set USERNAME_FIELD to 'email'.
#  you can define other fields that need to be filled out when creating a user by setting REQUIRED_FIELDS.
# Finally, Set the objects attribute to the custom manager we created.

import random
import string




class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=20)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # create a user manager to make queries to the database and manage users instances
    # and to call the Manager's methods to create users
    objects = UserManager()
    
    def __str__(self) -> str:
        return self.email


class Good(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    
    
    
class UserGoodRelation(models.Model):
    # many to one relation between relation model and user and good models 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    count = models.IntegerField()

    def save(self, *args, **kwargs):
        # Check if the related user and good exist, and create them if not
        if not self.user_id:
            password = result_str = ''.join(random.choice(string.ascii_letters) for i in range(9))
            self.user = User.objects.create_user(email='default@example.com',password=password)
        if not self.good_id:
            self.good = Good.objects.create(name='Default Good', price=random.randint(0,99999))
        super().save(*args, **kwargs)