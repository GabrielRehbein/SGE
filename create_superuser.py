import os
from decouple import config


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')


import django
django.setup()


from django.contrib.auth.models import User


DJANGO_ADM_USERNAME = config('DJANGO_ADM_USERNAME')
DJANGO_ADM_EMAIL = config('DJANGO_ADM_EMAIL')
DJANGO_ADM_PASSWORD = config('DJANGO_ADM_PASSWORD')


if not User.objects.filter(username=DJANGO_ADM_USERNAME).exists():
    user = User.objects.create_superuser(
    DJANGO_ADM_USERNAME,
    DJANGO_ADM_EMAIL,
    DJANGO_ADM_PASSWORD
    )
    print(f'Superuser {user.username} created with success.')
else:
    print('Superuser already exist.')
