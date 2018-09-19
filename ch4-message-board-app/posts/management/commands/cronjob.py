from django.core.management.base import BaseCommand

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Test cron job activated in Dockerfile'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        logger.info('Logging cron job')
        print('Running cron job...')
