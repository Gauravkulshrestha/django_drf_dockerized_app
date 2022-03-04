from django.db import models

class ToDo(models.Model):
    name = models.CharField(max_length=120)