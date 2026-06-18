# Generated manually for crawler change detection.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0033_repository_repo_introduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='pushed_at',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
