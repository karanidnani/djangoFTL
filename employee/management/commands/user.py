# Factory

import factory  
import factory.django
from employee.models import User, ActivityPeriod
from django.db import models
from django.db.models import Model
# factory.Faker._DEFAULT_LOCALE = 'en_US'
from django.conf.global_settings import LANGUAGES

class UserFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

class ActivityPeriodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ActivityPeriod

    start_time = factory.Faker('date_time')
    end_time = factory.Faker('date_time')
