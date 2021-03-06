# Generated by Django 2.2.7 on 2020-05-22 18:51

import commons.filters
from django.db import migrations, models
import functools


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer', models.CharField(max_length=120, verbose_name='Ofertante')),
                ('title', models.CharField(max_length=220, verbose_name='Nombre del puesto')),
                ('description', models.TextField(max_length=2000, verbose_name='Texto de la oferta')),
                ('salary', models.CharField(max_length=80, verbose_name='Salario o rango salarial')),
                ('contract_type', models.CharField(choices=[('IND', 'Indefinido'), ('Temporal', [('TEV', 'Eventual'), ('TOS', 'Por obras y servicios'), ('TDI', 'De interinidad'), ('TDR', 'De relevo')]), ('DFA', 'De formación y aprendizaje'), ('DPR', 'De prácticas'), ('OTR', 'Otro')], default='IND', max_length=3, verbose_name='Tipo de contrato')),
                ('work_mode', models.CharField(choices=[('RM', 'Remoto'), ('PR', 'Presencial'), ('MX', 'Mixto Remoto/Presencial'), ('NA', 'Sin determinar / Desconocido')], max_length=2, verbose_name='Remoto/Presencial')),
                ('part_time', models.BooleanField(default=False, verbose_name='A tiempo parcial')),
                ('more_info', models.URLField(blank=True, max_length=250, verbose_name='Enlace para más información')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('valid_until', models.DateField(blank=True, default=functools.partial(commons.filters.date_from_now, *(), **{'days': 91}), verbose_name='Válido hasta')),
                ('approved', models.BooleanField(default=False, verbose_name='Aprobada')),
            ],
            options={
                'verbose_name': 'Oferta de trabajo',
                'verbose_name_plural': 'Ofertas de trabajo',
                'db_table': 'job_offer',
            },
        ),
    ]
