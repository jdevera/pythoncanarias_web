# Generated by Django 2.1 on 2018-08-30 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='photo',
            field=models.ImageField(blank=True, default='speakers/speaker/noavatar.png', upload_to='speakers/speaker/'),
        ),
    ]
