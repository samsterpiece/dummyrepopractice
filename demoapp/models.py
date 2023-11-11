from django.db import models


class Widget(models.Model):
    name = models.CharField(max_length=140)

    objects = models.Manager()