# Generated by Django 4.0.6 on 2022-07-28 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('breed', models.CharField(max_length=128)),
                ('likes_to_bark', models.BooleanField()),
            ],
        ),
    ]