from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', default=0, on_delete=models.CASCADE)
    zipcode = models.IntegerField(max_length=10)
