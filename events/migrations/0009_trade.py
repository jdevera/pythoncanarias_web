# Generated by Django 2.1.3 on 2018-11-13 16:57

from django.db import migrations, models
import events.time_utils
import functools
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20181111_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sell_code', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('buy_code', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('start_at', models.DateTimeField(default=events.time_utils.now)),
                ('finish_at', models.DateTimeField(default=functools.partial(events.time_utils.now_plus, *(), **{'hours': 3}))),
                ('fixed_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('finished', models.BooleanField(default=False)),
                ('sucessful', models.BooleanField(default=False)),
            ],
        ),
    ]
