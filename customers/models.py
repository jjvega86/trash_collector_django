from django.db import models


class Customer(models.Model):
    PICKUP_DAYS = (
        ('Mo', 'Monday'),
        ('Tu', 'Tuesday'),
        ('We', 'Wednesday'),
        ('Th', 'Thursday'),
        ('Fr', 'Friday'),
    )
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', default=None, on_delete=models.CASCADE)
    address = models.ForeignKey('customers.Address', default=None, null=True, on_delete=models.CASCADE)
    account = models.ForeignKey('customers.Account', default=None, null=True, on_delete=models.CASCADE)
    weekly_pickup = models.CharField(max_length=2, choices=PICKUP_DAYS, null=True, default='Mo')
    extra_pickup = models.DateField(null=True)
    suspension_start = models.DateField(null=True)
    suspension_end = models.DateField(null=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    building_number = models.IntegerField()
    street_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()


class Account(models.Model):
    account_number = models.IntegerField()
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)
    last_charge = models.DateField(null=True)
