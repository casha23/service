from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Request(models.Model):
    NEW = 0
    IN_WORK = 1
    DONE = 2
    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_WORK, 'In work'),
        (DONE, 'Done')
    ]

    user = models.ForeignKey(
        User,
        related_name='requests',
        on_delete=models.SET_NULL,
        null=True
    )
    phone_model = models.CharField(max_length=150, blank=True)
    problem_description = models.TextField(blank=True)
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES,
        default=NEW,
    )
