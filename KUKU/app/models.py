from django.db import models

# Create your models here.

class Picture(models.Model):
    like = models.IntegerField(default=0)
    title = models.CharField(max_length=10, null=False)
    phone = models.CharField(max_length=20, null=True)
    category = models.CharField(max_length=20, null=False)
    address = models.TextField()
    fm = models.CharField(max_length=8, null=False)

class Visitors(models.Model):
    visited = models.IntegerField()