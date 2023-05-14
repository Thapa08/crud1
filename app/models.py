from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255,null=True,blank=True)
    phone_number = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.firstname