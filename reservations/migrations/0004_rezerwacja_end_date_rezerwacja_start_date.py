# Generated by Django 5.0.6 on 2024-05-19 11:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0003_rezerwacja"),
    ]

    operations = [
        migrations.AddField(
            model_name="rezerwacja",
            name="end_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="rezerwacja",
            name="start_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
