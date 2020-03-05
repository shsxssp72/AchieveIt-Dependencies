from django.db import models


class Personnel(models.Model):
    user_id = models.BigIntegerField(unique=True, primary_key=True)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=255)
    user_department = models.CharField(max_length=50)
    user_telephone = models.CharField(max_length=15)


class Customers(models.Model):
    customer_id = models.CharField(max_length=15, primary_key=True)
    referred_coordinator_id = models.BigIntegerField()
    corporation_name = models.CharField(max_length=255)
    customer_level = models.CharField(max_length=10)
    customer_email = models.CharField(max_length=255)
    customer_telephone = models.CharField(max_length=15)
    customer_address = models.CharField(max_length=255)
