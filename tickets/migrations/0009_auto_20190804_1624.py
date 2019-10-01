# Generated by Django 2.2.4 on 2019-08-04 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_event_closed_schedule'),
        ('tickets', '0008_auto_20190726_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='can_be_awarded',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Raffle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='raffle', to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Present',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True)),
                ('awarded_at', models.DateTimeField(blank=True, null=True)),
                ('awarded_ticket', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='present', to='tickets.Ticket')),
                ('raffle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presents', to='tickets.Raffle')),
            ],
        ),
    ]