from django.db import models

# Create your models here.
class Jobs(models.Model):
    Images=models.ImageField(upload_to='images/')
    Summary=models.CharField(max_length=200)

