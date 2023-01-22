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

    def __str__(self):
        return f"{self.phone_model} for {self.user}"


class Invoice(models.Model):
    UNPAID = 0
    PAID_UP = 1
    STATUS_CHOICES = [
        (UNPAID, 'Unpaid'),
        (PAID_UP, 'Paid-up')
    ]

    master = models.ForeignKey(
        User,
        related_name='invoices',
        on_delete=models.SET_NULL,
        null=True
    )
    request = models.ForeignKey(
        Request,
        related_name='invoices',
        on_delete=models.SET_NULL,
        null=True
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES,
        default=UNPAID,
    )

    def __str__(self):
        return f"Invoice to {self.request}"
