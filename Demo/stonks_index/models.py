from django.db import models

# Create your models here.
class DBTest(models.Model):
    test = models.CharField(max_length=100, primary_key=True)