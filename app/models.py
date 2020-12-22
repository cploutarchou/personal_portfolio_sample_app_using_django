from datetime import datetime
from django.db import models


class MenuGroup(models.Model):
    title = models.CharField(max_length=10)


class Menu(models.Model):
    parent_id = models.SmallIntegerField(3)
    title = models.CharField(max_length=100)
    position = models.SmallIntegerField(2)
    group_id = models.ForeignKey(MenuGroup, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now())
    prefix = models.CharField(max_length=250)
    order = models.SmallIntegerField(2)
    active = models.BooleanField(default=True)


class Settings(models.Model):
    name = models.CharField(max_length=250, unique=True)
    value = models.TextField()
    active = models.BooleanField(default=True, db_index=True)
