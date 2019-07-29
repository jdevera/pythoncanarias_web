# Generated by Django 2.2 on 2019-07-29 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='retention',
            field=models.IntegerField(choices=[(0, 'NO RETENTION'), (1, 'IRPF 6%'), (2, 'IRPF 12%'), (3, 'IRPF 21%')], default=0),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='taxes',
            field=models.IntegerField(choices=[(0, 'exto IGIC'), (1, 'IGIC (7%)'), (2, 'iva (21%)')], default=0),
        ),
    ]
