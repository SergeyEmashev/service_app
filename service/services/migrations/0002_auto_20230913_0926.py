# Generated by Django 3.2.16 on 2023-09-13 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Subscription', to='clients.client')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Subscription', to='services.plan')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Subscription', to='services.service')),
            ],
        ),
        migrations.DeleteModel(
            name='Subscrition',
        ),
    ]
