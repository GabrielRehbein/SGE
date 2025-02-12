from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from decouple import config


DJANGO_ADM_USERNAME = config('DJANGO_ADM_USERNAME')
DJANGO_ADM_EMAIL = config('DJANGO_ADM_EMAIL')
DJANGO_ADM_PASSWORD = config('DJANGO_ADM_PASSWORD')

class Command(BaseCommand):
    help = 'Creates a superuser with predefined credentials.'

    def handle(self, *args, **options):
        try:
            if not User.objects.filter(username=DJANGO_ADM_USERNAME).exists():
                superuser = User.objects.create_superuser(
                    DJANGO_ADM_USERNAME,
                    DJANGO_ADM_EMAIL,
                    DJANGO_ADM_PASSWORD
                )
                superuser.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Superuser {superuser.username} created successfully!')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Superuser {superuser.username} already exists!')
                )
        except Exception as e:
            self.style.ERROR(f'ERROR: {e}')
