from datetime import datetime

from django.db import models


# Create your models here.
class MainMenu(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(datetime.now())
    active = models.BooleanField("True")


class Posts(models.Model):
    pass
