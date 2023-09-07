from django.shortcuts import render
from django.http import HttpResponse

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