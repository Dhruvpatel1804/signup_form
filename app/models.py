from django.db import models

# Create your models here.
class Contactmodel(models.Model):
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    Phonenumber = models.CharField(max_length=12)
    password = models.CharField(max_length=8)

    def __str__(self):
         return self.Firstname