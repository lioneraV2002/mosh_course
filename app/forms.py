from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
# from .models import User

# To view our custom user models in the admin panel
# we need to create forms.


# get the current user active
User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
