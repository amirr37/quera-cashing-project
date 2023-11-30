from django.urls import path
from .views import CreateTransactionAPIView, UpdateTransactionAPIView, UserTransactionsAPIView, \
    UserTransactionDetailAPIView, DeleteUserTransactionAPIView, CategoryListView

urlpatterns = [
    path('create-transaction/', CreateTransactionAPIView.as_view(), name='create-transaction-api'),
    path('update-transaction/<int:pk>/', UpdateTransactionAPIView.as_view(), name='update-transaction-api'),
    path('user-transactions/', UserTransactionsAPIView.as_view(), name='user-transactions-api'),
    path('user-transaction/<int:pk>/', UserTransactionDetailAPIView.as_view(), name='user-transaction-detail-api'),
    path('delete-user-transaction/<int:pk>/', DeleteUserTransactionAPIView.as_view(),
         name='delete-user-transaction-api'),
    path('categories/', CategoryListView.as_view(), name='category-list-api'),

]
