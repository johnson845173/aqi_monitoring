# Generated by Django 4.1.2 on 2023-02-20 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0006_remove_attendance_details_student_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_details',
            old_name='Name',
            new_name='name',
        ),
    ]
