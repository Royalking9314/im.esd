from django.db import models
from django.urls import reverse

class User(models.Model):
    account_type = models.CharField(max_length=100)
    account_number = models.IntegerField(unique=True,null=False,db_default=0)
    ifsc_code = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f"{self.account_type} - {self.account_number} - {self.ifsc_code}"

    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])