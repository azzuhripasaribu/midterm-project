import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Feedback(models.Model):
    # name, message
    name = models.CharField(max_length=100)
    message = models.TextField()
