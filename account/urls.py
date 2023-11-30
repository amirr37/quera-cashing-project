from django.urls import path

from account.views import CustomUserCreateAPIView

urlpatterns = [
    path('create-user/', CustomUserCreateAPIView.as_view(), name='customuser-create'),

]



