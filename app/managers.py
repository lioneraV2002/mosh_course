from django.contrib.auth.base_user import BaseUserManager

# the manager helps with database query operations.
# to save users in database

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('the email must be set')
        email = self.normalize_email(email=email)
        # creating user instance
        user = self.model(email= email, **extra_fields)
        user.set_password(password)
        # saving user to the database (made a query)
        user.save()
        
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        # set these fields by default 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        # check if they are explicitly mentioned
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        # calling create_user method above 
        return self.create_user(email, password, **extra_fields)
    