# Generated by Django 4.2.11 on 2024-08-14 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_student_github_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administration',
            name='github_id',
        ),
    ]
