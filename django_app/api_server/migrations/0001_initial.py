# Generated by Django 4.1.4 on 2022-12-31 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Datetime', models.DateTimeField(auto_created=True)),
                ('PM', models.FloatField()),
                ('NO', models.FloatField()),
                ('NO2', models.FloatField()),
                ('NOx', models.FloatField()),
                ('CO', models.FloatField()),
                ('SO2', models.FloatField()),
                ('O3', models.FloatField()),
                ('AQI', models.FloatField()),
            ],
        ),
    ]
