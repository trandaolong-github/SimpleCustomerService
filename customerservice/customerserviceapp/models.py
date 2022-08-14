from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from .managers import CustomUserManager


class Ticket(models.Model):
    PACKING = 1
    DONE = 2

    STATUS = (
        (PACKING, "Đang lấy hàng"),
        (DONE, "Đã giao hàng")
    )
    customer = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS)
    quantity1 = models.FloatField()
    quantity2 = models.FloatField()
    quantity3 = models.FloatField()
    quantity4 = models.FloatField()

    def __str__(self):
        return str(self.id)


class CustomUser(AbstractUser):
    is_receiver = models.BooleanField(default=False)
    is_distributor = models.BooleanField(default=False)

    objects = CustomUserManager()
