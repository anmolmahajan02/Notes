# Generated by Django 5.1.6 on 2025-02-28 17:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
