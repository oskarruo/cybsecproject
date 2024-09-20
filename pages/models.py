from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    date = models.DateField()
    starttime = models.IntegerField()
    endtime = models.IntegerField()
    title = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
