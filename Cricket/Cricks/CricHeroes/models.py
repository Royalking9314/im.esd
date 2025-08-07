from django.db import models

# Create your models here.
class User(models.Model):    ##STEP 2
   name = models.CharField(max_length=100)
   virtual_id = models.EmailField(max_length=100,unique=True)
   password = models.CharField(max_length=100)

   def _str_(self):
       return f"{self.name} - {self.virtual_id} - {self.password}"
