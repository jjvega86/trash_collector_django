from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer


# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # query for customer object
    # IF customer does not exist, call create function
    # ELSE, pass customer object as context to render function
    # get the logged in user within any view function
    user = request.user
    customer = Customer.objects.filter(user=user)
    if not customer:
        create(request, user)
    else:
        context = {
            'customer': customer
        }
        return render(request, 'customers/index.html', context)


def create(request, user):
    # assign user as customer user foreign key
    # add customer name to customer object
    # use helper function to add address to new address object
    # use helper function to generate address and add as foreign key
    if request.method == 'POST':
        name = request.POST.get('name')

        customer = Customer()
        customer.user = user
        customer.name = name



