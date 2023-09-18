from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import User

# To view our custom user models in the admin panel
# we need to create forms.


# get the current user active
user = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = user
        fields = '__all__'
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = user
        fields = '__all__'





from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')

class AddGoodsForm(forms.ModelForm):
    class Meta:
        model = UserGoodRelation
        fields = ('good', 'count')

