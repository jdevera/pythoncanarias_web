# Generated by Django 2.2.7 on 2019-12-01 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0014_auto_20191201_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='active',
        ),
    ]
