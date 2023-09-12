from django.urls import path

# so we can reference our view functions
from . import views



# URLConf module
# should include this url conf in the main url configuration
urlpatterns = [
    path('hello/', view=views.say_hello),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('add_goods/', views.add_goods, name='add_goods'),
    path('logout/', views.user_logout, name='logout'),

]
