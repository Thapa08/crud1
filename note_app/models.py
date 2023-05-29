from django.db import models

# Create your models here.
class Notes(models.Model):
    heading = models.CharField(max_length=200,verbose_name='Title')
    content = models.CharField(max_length=1000,verbose_name='Content')
    def __str__(self):
        return self.heading