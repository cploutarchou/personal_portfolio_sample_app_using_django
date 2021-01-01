from django.utils.timezone import localtime, now
from django.db import models
from datetime import timezone, timedelta


class MenuGroup(models.Model):
    title = models.CharField(max_length=10)


class Menu(models.Model):
    parent_id = models.SmallIntegerField(3)
    title = models.CharField(max_length=100)
    position = models.SmallIntegerField(2)
    group_id = models.ForeignKey(MenuGroup, on_delete=models.CASCADE)
    created_at = models.DateTimeField(localtime)
    prefix = models.CharField(max_length=250)
    order = models.SmallIntegerField(2)
    active = models.BooleanField(default=True)


class Settings(models.Model):
    name = models.CharField(max_length=250, unique=True)
    value = models.TextField()
    active = models.BooleanField(default=True, db_index=True)


class Posts(models.Model):
    author = models.BigIntegerField(default=0)
    submitted_date = models.DateTimeField(name="Status")
    context = models.TextField()
    title = models.CharField(max_length=150)

    class Status(models.TextChoices):
        PUB = '1', "Publish"
        SAVE = '2', "Save"
        DRAFT = '3', "Draft"
        PUBED = '4', "Published"

    month = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )
