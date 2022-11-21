from django.db import models
from django import forms

# Create your models here.

class UserEntries(models.Model):
    input_one = models.CharField(max_length=1000)
    input_two = models.CharField(max_length=1000)


    def __str__(self):
        return self.input_one, self.input_two

