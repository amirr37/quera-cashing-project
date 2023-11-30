from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Sum, FloatField, DecimalField
from django.db.models.functions import Coalesce
from django.db.models.lookups import IntegerFieldFloatRounding
from rest_framework.fields import IntegerField
from django.db.models import FloatField, F


# Create your models here.

# ----------------------------------------------------------------
# superuser info
# username= amirr37
# password=admin
# ----------------------------------------------------------------

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.username

    def update_balance(self):
        total_income = self.calculate_total_income()

        total_expense = self.calculate_total_expense()
        print(total_income)
        print(total_expense)
        print("111")
        self.balance = total_income - total_expense
        print("2222")
        print(self.balance)

        self.save()
        print("3333333")
        print(self.balance)
        return self.balance

    def calculate_total_income(self):
        total_income = self.transaction_set.filter(type='income').aggregate(
            Sum('amount', default=0))
        total_income = float(total_income['amount__sum'])
        return total_income

    def calculate_total_expense(self):
        total_expense = self.transaction_set.filter(type='expense').aggregate(
            Sum('amount', default=0))
        total_expense = float(total_expense['amount__sum'])
        return total_expense
