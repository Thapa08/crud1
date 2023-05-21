from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.IntegerField( null=True ,blank = True)

    def __str__(self):
        return self.firstname
    
