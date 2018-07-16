# Generated by Django 2.0.7 on 2018-07-16 16:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_tickettype_release_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='sold_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
