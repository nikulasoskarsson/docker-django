from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=40)
    body = models.CharField(max_length=255)
