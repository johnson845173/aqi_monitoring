# Generated by Django 4.1.4 on 2023-02-19 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0003_attendance_details_student_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance_details',
            name='attendence_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
