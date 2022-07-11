from django.db import models
from django.contrib.auth.models import User


class Players(models.Model):
    name = models.CharField("Name", max_length=50, null=True)
    about = models.CharField("About", max_length=100, null=True)
    debuts = models.CharField("Debuts", max_length=50, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Debuts(models.Model):
    name = models.CharField("Name", max_length=50, null=True)
    about = models.CharField("About", max_length=2000, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Opening(models.Model):
    name = models.CharField("Name", max_length=50, null=True)
    about = models.CharField("About", max_length=2000, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField("Title", max_length=100, null=True)
    about = models.TextField()
    author = models.CharField("Author", max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
