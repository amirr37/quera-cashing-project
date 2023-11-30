from django.db import models
from django.db.models import F
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from account.models import CustomUser


# todo : balance for updating transactions


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} - {self.amount} on {self.created_at}"

    def save(self, *args, **kwargs):
        print("saveeeeeeeeeeeeeeeee")
        self.user.update_balance()
        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.user.update_balance()
