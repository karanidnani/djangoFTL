# Factory
import random
import factory
import factory.django
from employee.models import User, ActivityPeriod
from django.db import models
from django.db.models import Model


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    #country = factory.Faker('country')

class ActivityPeriodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ActivityPeriod

    start_time = factory.Faker('date_time')
    end_time = factory.Faker('date_time')