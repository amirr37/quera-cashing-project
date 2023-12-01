from django.db import models
from django.db.models import F, Sum
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from account.models import CustomUser




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
        self.user.update_balance()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.user.update_balance()


class Report(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_income = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_expense = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        abstract = True

    def calculate_total_income(self):
        raise NotImplementedError("Subclasses must implement this method")

    def calculate_total_expense(self):
        raise NotImplementedError("Subclasses must implement this method")


class MonthlyReport(Report):
    start_date = models.DateField()
    end_date = models.DateField()

    def calculate_total_income(self):
        transactions = Transaction.objects.filter(
            user=self.user,
            type='income',  # Adjust based on your Transaction model
            created_at__range=(self.start_date, self.end_date)
        )
        total_income = transactions.aggregate(Sum('amount'))['amount__sum'] or 0
        self.total_income = total_income
        return total_income

    def calculate_total_expense(self):
        transactions = Transaction.objects.filter(
            user=self.user,
            type='expense',  # Adjust based on your Transaction model
            created_at__range=(self.start_date, self.end_date)
        )
        total_expense = transactions.aggregate(Sum('amount'))['amount__sum'] or 0
        self.total_expense = total_expense
        return total_expense

    def save(self, *args, **kwargs):
        # Calculate and set total_income and total_expense before saving
        self.calculate_total_income()
        self.calculate_total_expense()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - Monthly Report ({self.start_date} to {self.end_date})"
