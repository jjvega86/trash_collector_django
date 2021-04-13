from django.db import models
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    PICKUP_DAYS = (
        ('Mo', 'Monday'),
        ('Tu', 'Tuesday'),
        ('Mo', 'Wednesday'),
        ('Mo', 'Thursday'),
        ('Mo', 'Friday'),
    )
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', default=0, on_delete=models.CASCADE)
    address = models.ForeignKey('customers.Address', default=0, on_delete=models.CASCADE)
    weekly_pickup = models.CharField(max_length=2)


class Address(models.Model):
    building_number = models.IntegerField(max_length=10)
    street_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField(max_length=10)


