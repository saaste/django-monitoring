# Generated by Django 4.0.6 on 2022-07-29 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='is_test',
            field=models.BooleanField(default=False),
        ),
    ]
