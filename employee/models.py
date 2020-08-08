from django.db import models
from django.db.models import Model
from django.utils import timezone
import datetime

class ActivityPeriod(models.Model):
    start_time = models.DateTimeField(default=datetime.date.today)
    end_time = models.DateTimeField(default=datetime.date.today)


class User(models.Model):
    #activityperiod = models.ForeignKey('ActivityPeriod', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25, default="Some string", editable=False)
    last_name = models.CharField(max_length=25,default="Some string",editable=False)