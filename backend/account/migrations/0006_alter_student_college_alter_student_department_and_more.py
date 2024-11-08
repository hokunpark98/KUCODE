# Generated by Django 4.2.11 on 2024-05-21 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='college',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='double_major',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='enrollment',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='primary_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='secondary_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]