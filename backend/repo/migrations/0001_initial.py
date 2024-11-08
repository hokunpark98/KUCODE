# Generated by Django 4.2.11 on 2024-05-13 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('owner_github_id', models.CharField(max_length=50)),
                ('created_at', models.CharField(max_length=100)),
                ('updated_at', models.CharField(max_length=100)),
                ('fork_count', models.IntegerField(null=True)),
                ('star_count', models.IntegerField(null=True)),
                ('commit_count', models.IntegerField(null=True)),
                ('open_issue_count', models.IntegerField(null=True)),
                ('closed_issue_count', models.IntegerField(null=True)),
                ('languate', models.CharField(max_length=100)),
                ('contributor', models.CharField(max_length=100)),
                ('license', models.CharField(max_length=100)),
                ('has_readme', models.BooleanField()),
                ('description', models.CharField(max_length=100)),
                ('release_version', models.CharField(max_length=100)),
                ('etc', models.CharField(max_length=100)),
                ('github_id', models.CharField(max_length=50)),
            ],
        ),
    ]