from django.contrib import admin


# Register your models here.
# In the admin.py file, 
# we are configuring the Django admin panel
# to work with our custom user model


from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Good, UserGoodRelation

from .user_forms import CustomUserCreationForm, CustomUserChangeForm


# get the current user active
User = get_user_model()


# @admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    
    list_display = ['email','first_name','last_name', 'is_staff', 'is_active']
    list_filter = ['email', 'is_staff', 'is_active']
    fieldsets = [
        (
            None,
            {
                'fields': ['email', ('first_name', 'last_name'), 'last_login', 'date_joined'],
            },
        ),
        (
            'Advanced options',
            {
                'classes': ['collapse'],
                'fields': ['password', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'],
            },
        ),
    ]
    add_fieldsets = [
        (
            None,
            {
                'fields': ['email', ('first_name', 'last_name'), 'password1', 'password2'],
            },
        ),
        (
            'Advanced options',
            {
                'classes': ['collapse'],

                'fields': ['is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'],
            },
        ),
    ]
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'date_joined', 'last_login')

    

admin.site.register(User,CustomUserAdmin)



class GoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']


admin.site.register(Good, GoodAdmin)



class UserGoodRelationAdmin(admin.ModelAdmin):
    list_display = ('user', 'good', 'count', 'is_available')
    list_filter = ('user', 'good')
    search_fields = ('user__email', 'good__name')

admin.site.register(UserGoodRelation, UserGoodRelationAdmin)
