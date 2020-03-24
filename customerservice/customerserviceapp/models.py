from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Ticket(models.Model):
    INBACKLOG = 1
    INPROGRESS = 3
    DONE = 4

    STATUS = (
        (INBACKLOG, "In backlog"),
        (INPROGRESS, "In progress"),
        (DONE, "Done")
    )
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.PROTECT, null=True)
    ticket = models.ForeignKey(Ticket, related_name='ticket', on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=10000)

    def __str__(self):
        return str(self.id)