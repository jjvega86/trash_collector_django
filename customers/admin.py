from django.contrib import admin
from .models import Customer
from .models import Account
from .models import Address

# Register your models here.


admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Address)
