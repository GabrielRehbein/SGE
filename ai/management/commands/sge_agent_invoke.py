from django.core.management.base import BaseCommand
from ai.agents import SGEAgent


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            agent_ai = SGEAgent()
            agent_ai.invoke()
            self.stdout.write(self.style.SUCCESS('SGE AGENT INVOCADO COM SUCESSO!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'ERRO AO INVOCAR SGE AGENT: {str(e)}'))