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






from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import MonthlyReport
from .serializers import MonthlyReportSerializer
from datetime import datetime

class MonthlyReportCreateAPIView(generics.CreateAPIView):
    serializer_class = MonthlyReportSerializer

    def create(self, request, *args, **kwargs):
        start_date_str = request.data.get('start_date')
        end_date_str = request.data.get('end_date')

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        if start_date > end_date:
            return Response({'error': 'End date must be equal to or after the start date.'}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user  # Assuming you are using authentication

        # Check if a report already exists for the given period
        existing_report = MonthlyReport.objects.filter(user=user, start_date=start_date, end_date=end_date).first()

        if existing_report:
            serializer = MonthlyReportSerializer(existing_report)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # If no existing report, create a new one
        report_data = {
            'user': user.id,
            'start_date': start_date,
            'end_date': end_date,
        }

        serializer = MonthlyReportSerializer(data=report_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
