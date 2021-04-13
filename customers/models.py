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
    user = models.ForeignKey('accounts.User', default=0, on_delete=models.CASCADE)
    address = models.ForeignKey('customers.Address', default=0, on_delete=models.CASCADE)
    account = models.ForeignKey('customers.Account', default=0, on_delete=models.CASCADE)
    weekly_pickup = models.CharField(max_length=2, choices=PICKUP_DAYS)
    extra_pickup = models.DateField()
    suspension_start = models.DateField()
    suspension_end = models.DateField()

    def __str__(self):
        return self.name


class Address(models.Model):
    building_number = models.IntegerField(max_length=10)
    street_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField(max_length=10)


class Account(models.Model):
    account_number = models.IntegerField()
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)
