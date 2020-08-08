from django.core.management.base import BaseCommand

from .user import UserFactory
from .user import ActivityPeriodFactory

class Command(BaseCommand):
    help = 'Populates the database.'

    def add_arguments(self, parser):
        parser.add_argument('--users',
            default=200,
            type=int,
            help='The number of fake users to create.')

    def handle(self, *args, **options):
        for _ in range(options['users']):
            UserFactory.create()
            #ActivityPeriodFactory.create()