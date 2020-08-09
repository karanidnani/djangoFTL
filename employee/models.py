from django.db import models
from django.db.models import Model
from django.utils import timezone
import datetime
from django_countries.fields import CountryField

class ActivityPeriod(models.Model):
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True)

class User(models.Model):
    first_name = models.CharField(max_length=25,default="Some string",null=True)
    last_name = models.CharField(max_length=25,default="Some string",null=True)