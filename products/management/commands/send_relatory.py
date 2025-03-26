from django.core.management.base import BaseCommand
from services.notify import Notify
class Command(BaseCommand):
    help = 'send relatory for whatsapp'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('READY')
        )
