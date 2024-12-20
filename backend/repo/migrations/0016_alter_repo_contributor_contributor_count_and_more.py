# Generated by Django 4.2.11 on 2024-05-25 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0015_repo_contributor_contributor_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repo_contributor',
            name='contributor_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='repo_contributor',
            name='owner_github_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='repo_contributor',
            name='repo_url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
