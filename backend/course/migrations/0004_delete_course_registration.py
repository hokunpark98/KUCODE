# Generated by Django 4.2.11 on 2024-05-14 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_rename_course_id_course_registration_course_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course_registration',
        ),
    ]
