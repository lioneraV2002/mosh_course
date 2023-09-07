from django.contrib import admin


# Register your models here.
# In the admin.py file, 
# we are configuring the Django admin panel
# to work with our custom user model


from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import *

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User