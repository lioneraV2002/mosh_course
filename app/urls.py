from django.urls import path

# so we can reference our view functions
from . import views



# URLConf module
# should include this url conf in the main url configuration
urlpatterns = [
    path('hello/', view=views.say_hello)
]
