from rest_framework import serializers
from .models import Transaction, Category, MonthlyReport


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MonthlyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyReport
        fields = ['id', 'user', 'start_date', 'end_date', 'total_income', 'total_expense']
        read_only_fields = ['total_income', 'total_expense']
