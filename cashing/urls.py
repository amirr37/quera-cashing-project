from django.urls import path
from .views import CreateTransactionAPIView

urlpatterns = [
    path('create-transaction/', CreateTransactionAPIView.as_view(), name='create-transaction-api'),
    # Other URLs
]


