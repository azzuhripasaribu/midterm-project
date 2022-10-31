import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LandingPage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    header = models.CharField(max_length=250)
    body = models.TextField()