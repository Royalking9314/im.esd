from django.db import models

# Create your models here.
class User(models.Model):
   name = models.CharField(max_length=100)
   type = models.EmailField(max_length=100)
   race_length = models.IntegerField()

   def __str__(self):
       return f"{self.name} - {self.type} - {self.race_length}"