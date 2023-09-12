from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .forms import *

from django.contrib.auth.decorators import login_required

# Create your views here.
# it is a request handler not the view we normally see


# a view function is a function that takes a request and returns a response
# a request handler
# action

def say_hello(request):
    # return HttpResponse('Hello World!')
    x = calculate()
    y = 2
    return render(request, 'hello.html',context={'name': 'Kamyar'})
    


def calculate():
    x = 1
    y = 2
    return x




# registration view method, gets a request,
# makes a form out of it
# and does the saving process of the entered information
# then redirects you to login page
# if request form is not valid, then, it passes an instance of the form to the render method with register.html file to be rendered 
# and wait to get the input from data

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        # print(request.POST)
        print(form.errors)

        if form.is_valid():
            new_user = form.save()
            # login(request, new_user)
            print(new_user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})



# login view method, gets a request,
# makes a form out of it
# and checks whether it is valid or not.
# if valid, it logs the user in and redirect them to the add_goods page
# if not, then, an instance of the form is created, passed to the render method along with login.html file to be rendered with
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        print(form.errors)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Correct way to authenticate user
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('add_goods')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




@login_required
def add_goods(request):
    if request.method == 'POST':
        form = AddGoodsForm(request.POST)
        if form.is_valid():
            # Get the selected good and count from the form
            selected_good = form.cleaned_data['good']
            count = form.cleaned_data['count']
            
            # Check if the user already has a UserGoodRelation for the selected good
            user_good_relation, is_created = UserGoodRelation.objects.get_or_create(user=request.user, good=selected_good, defaults={'count':0})
            
            # Update the count for the UserGoodRelation
            # i encountered an integrity error for the count field
            if is_created:
                user_good_relation.count = count
            else:
                user_good_relation.count += count
            
            user_good_relation.save()
            
            # Redirect to the add goods page or any other page you prefer
            return redirect('add_goods')
    
    else:
        form = AddGoodsForm()
    all_goods = UserGoodRelation.objects.all()
    user_goods = UserGoodRelation.objects.filter(user=request.user)
    return render(request, 'add_goods.html', {'form': form, 'user_goods': user_goods, 'all_goods':all_goods})





def user_logout(request):
    logout(request)
    return redirect('login')
