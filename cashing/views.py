from django.shortcuts import render

# Create your views here.


# user transactions crud + filter

from django_filters.rest_framework import DjangoFilterBackend  # Import the correct backend
from rest_framework import generics

from .filters import TransactionFilter
from .models import Transaction, Category
from .serializers import TransactionSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated


# region Transaction

class CreateTransactionAPIView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdateTransactionAPIView(generics.UpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


class UserTransactionsAPIView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = TransactionFilter
    filter_backends = [DjangoFilterBackend]  # Use the correct backend

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


class UserTransactionDetailAPIView(generics.RetrieveAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


class DeleteUserTransactionAPIView(generics.DestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


# endregion


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


