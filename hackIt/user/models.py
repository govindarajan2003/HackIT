# user/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    date_of_birth = models.DateField(default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.email}"
