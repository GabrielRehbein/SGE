# Generated by Django 5.1.5 on 2025-01-24 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inflows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inflow',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
