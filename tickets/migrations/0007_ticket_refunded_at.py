# Generated by Django 2.1.4 on 2019-04-21 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_ticket_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='refunded_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
