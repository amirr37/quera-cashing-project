import django_filters
from .models import Transaction

class TransactionFilter(django_filters.FilterSet):
    class Meta:
        model = Transaction
        fields = {
            'amount': ['exact', 'lt', 'lte', 'gt', 'gte'],
            'type': ['exact'],
            'category': ['exact'],
            'created_at': ['exact', 'lt', 'lte', 'gt', 'gte'],
        }
