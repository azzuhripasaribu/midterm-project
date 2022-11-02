from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Center(models.Model):
    name = models.TextField()
    website = models.URLField()
    email = models.EmailField()

    # @classmethod
    # def create(cls, name, website, email):
    #     center = cls(name = name, website = website, email = email)
    #     return center


class Area(models.Model):
    name = models.TextField(max_length=255)
    center = models.ManyToManyField(Center)

    @classmethod
    def create(cls, name):
        area = cls(name = name)
        return area
