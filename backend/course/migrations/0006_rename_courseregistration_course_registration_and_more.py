# Generated by Django 4.2.11 on 2024-05-14 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0003_alter_repository_contributor_and_more'),
        ('account', '0005_student'),
        ('course', '0005_courseregistration'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CourseRegistration',
            new_name='Course_registration',
        ),
        migrations.AlterUniqueTogether(
            name='course_registration',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='Course_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('repo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repo.repository')),
            ],
        ),
    ]