# Generated by Django 3.2.16 on 2023-09-14 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20230913_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
