# Generated by Django 3.2.17 on 2023-09-15 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_subscription_services_su_field_a_155836_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='field_a',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='field_b',
            field=models.CharField(default='', max_length=25),
        ),
    ]
