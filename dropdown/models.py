from django.db import models

# Create your models here.
class Dropdown(models.Model):
    dropdown=models.CharField(choices=(('Text','Text'),('Image','Image'),('Audio','Audio')),max_length=200,null=True,blank=True)
    textarea = models.CharField(max_length=20,verbose_name='Text')
    image = models.ImageField(verbose_name='Image',null=True,blank=True)
    audio = models.FileField(verbose_name='Audio',null=True,blank=True)
    def __str__(self):
        return self.name
