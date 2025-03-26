from django.core.management.base import BaseCommand
from outflows.models import Outflow
from django.utils import timezone
from datetime import timedelta
from services.callmebot import CallMeBotService
class Command(BaseCommand):
    help = 'send relatory for whatsapp'

    def handle(self, *args, **options):
        call_me_bot_client = CallMeBotService()
        now = timezone.now()

        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = now.replace(hour=23, minute=59, second=59, microsecond=999999)

        outflows_today = Outflow.objects.filter(
            created_at__range=[today_start, today_end]
        ).count()
        message = {
            'text': f'Hoje tivemos {outflows_today} vendas hoje!'
        }
        call_me_bot_client.send_message(message['text'])



