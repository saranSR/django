from django.db import models
from django.forms import FilePathField


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.TextField()
    cost = models.TextField()

    def __str__(self):
        return self.name