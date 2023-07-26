# .\main\models.py

from django.db import models

class VisitorData(models.Model):
    location = models.CharField(max_length=100)
    time_spent = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.location} - {self.time_spent} seconds'
