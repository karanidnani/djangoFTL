Description - Initially, project called karan_ftl is made which has an application viz. "employee".

The employee app consists of two models - User which has id, first_name, last_name and ActivityPeriod which has start_time, end_time.

The database (SQLite) is populated using Custom Management Tool which imports two Factories i.e. UserFactory and ActivityPeriodFactory from Faker. To generate the
fake data two Python files are created inside employee/management/commands. Once you initiate UserFactory.create(), ActivityPeriodFactory.create() database gets
populated.

As the database is populated, we now return this data in JSON format using REST API. To do this, serializers are made the respective model and the subsequent url
patterns are added. For users, the data is displayed on the home page itself whereas for the time url pattern is as localhost/time.

The Django app is hosted on pythonanywhere.com, to access it go to https://teampareto29.pythonanywhere.com for users.
For ActivityPeriod, go to https://teampareto29.pythonanywhere.com/time

The errors generated where:
1. Error - https://stackoverflow.com/questions/25958708/django-1-7-no-migrations-to-apply-when-run-migrate-after-makemigrations Initial migration was fake

2. Populate - https://stackoverflow.com/questions/33024510/populate-django-database

3. AttributeError: Unknown formatter "start_time" with locale "en_US"

4. https://stackoverflow.com/questions/36123312/django-operationalerror-at-admin

Currently both models are independent i.e. they aren't integrated.
