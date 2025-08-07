from django.db import models
from django.urls import reverse   # Import the reverse function
# Create your models here.
class User(models.Model):    ##STEP 2
   name = models.CharField(max_length=100)
   sport = models.CharField(max_length=100) ## e.g., Football, Basketball,Cricket
   age = models.IntegerField()

   def __str__(self):
       return f"{self.name} - {self.sport} - {self.age}"