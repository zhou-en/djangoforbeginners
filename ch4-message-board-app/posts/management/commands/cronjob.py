from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Test cron job activated in Dockerfile'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        print('Running cron job...')
