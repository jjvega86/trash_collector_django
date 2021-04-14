from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import helpers
from .models import Customer

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # query for customer object
    # IF customer does not exist, call create function
    # ELSE, pass customer object as context to render function
    # get the logged in user within any view function
    user = request.user
    customer = Customer.objects.filter(user=user)
    if not customer:
        return render(request, 'customers/create.html')
    else:
        context = {
            'customer': customer
        }
        return render(request, 'customers/index.html', context)


def create(request):
    # assign user as customer user foreign key
    # add customer name to customer object
    # use helper function to add address to new address object
    # use helper function to generate address and add as foreign key
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        customer = Customer()
        customer.user = user
        customer.name = name
        customer.save()
        helpers.create_address(customer, request)
        helpers.create_account(customer)
        return render(request, 'customers/index.html', context={
            'customer': customer
        })
    else:
        return render(request, 'customers/create.html')
