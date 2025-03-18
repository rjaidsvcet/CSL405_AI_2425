from django.db import models

# Create your models here.

class Firstname (models.Model):
    firstname = models.CharField (max_length=50)