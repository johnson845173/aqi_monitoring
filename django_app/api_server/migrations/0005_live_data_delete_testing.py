# Generated by Django 4.1.4 on 2023-02-19 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0004_attendance_details_attendence_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='live_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Datetime', models.DateTimeField(auto_created=True)),
                ('ch4', models.FloatField()),
                ('Coal', models.FloatField()),
                ('CO', models.FloatField()),
                ('Sulfur', models.FloatField()),
                ('butane', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Testing',
        ),
    ]
