from .models import Account, Address


def create_address(customer, request):
    building_number = request.POST.get("building_number")
    street_name = request.POST.get("street_name")
    city = request.POST.get("city")
    state = request.POST.get("state")
    zipcode = request.POST.get("zipcode")
    address = Address(building_number=building_number, street_name=street_name, city=city, state=state, zipcode=zipcode)
    address.save()
    customer.address = address
    customer.save()


def create_account(customer):
    accounts = Account.objects.all()
    accounts_count = accounts.count()
    account = Account(
        account_number=accounts_count + 1,
        account_balance=0,
        last_charge=None
    )
    account.save()
    customer.account = account
    customer.save()

