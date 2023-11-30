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

    ordering = django_filters.OrderingFilter(
        fields=(
            ('amount', 'amount'),
            ('created_at', 'created_at'),
            ('type', 'type'),
            ('category', 'category__title'),
            # Add more fields as needed
        ), )
