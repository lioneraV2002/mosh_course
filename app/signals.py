from django.db.models.signals import post_save
from django.dispatch import receiver
from app.models import *



# in short, signals associate events with actions
# Whenever a new user is saved in the database,
# it will call the user_created() method.
# this method, in fact, connects to a signal using the receiver decorator 
# after the Signal calls its send() method.
# we also require to register signals to apps.py file 
# since we made a signals file instead of using receivers directly in creation methods
# the type of the sender could be everything or something in particular like User bellow.


# In practice, signal handlers are usually defined in a signals submodule of the application they relate to.
# Signal receivers are connected in the ready() method of your application configuration class. If you’re using the receiver() decorator, 
# import the signals submodule inside ready().


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        print(f'A new Good was created: {instance.first_name}, {instance.last_name}, {instance.email}')
        



