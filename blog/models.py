from django.db import models

# Create your models here.
class Blog(models.Model):
    Title = models.CharField(max_length=200)
    Publication_Date = models.DateField()
    Body =  models.TextField()
    Images = models.ImageField(upload_to='images/')
