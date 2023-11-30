from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

# ----------------------------------------------------------------
# superuser info
# username= amirr37
# password=admin
# ----------------------------------------------------------------


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return self.username
