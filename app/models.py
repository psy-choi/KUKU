from django.db import models

# Create your models here.

class Picture(models.Model):
    like = models.IntegerField(default=0)
    title = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    address = models.TextField()

class Visitors(models.Model):
    visited = models.IntegerField()