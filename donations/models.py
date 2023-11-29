from django.db import models
from accounts.models import CustomUser
from django.utils import timezone


# Create your models here.

class Donate (models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    transaction_id = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.user.username} donated {self.amount} on {self.date.strftime('%d-%m-%Y')}"