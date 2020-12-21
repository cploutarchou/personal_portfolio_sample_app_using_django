from datetime import datetime

from django.db import models


# Create your models here.
class Menu(models.Model):
    parent_id = models.IntegerField(3)
    title = models.CharField(max_length=100)
    position = models.IntegerField(2)
    group_id = models.IntegerField(5)
    created_at = models.DateTimeField(datetime.now())
    prefix = models.CharField(max_length=250)
    order = models.IntegerField(2)
    active = models.BooleanField("True")


class MenuGroup(models.Model):
    title = models.CharField(max_length=10)


class Posts(models.Model):
    pass
