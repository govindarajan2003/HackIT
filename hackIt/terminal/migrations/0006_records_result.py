# Generated by Django 4.1.13 on 2024-03-16 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0005_alter_records_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='result',
            field=models.CharField(default=None, max_length=5000),
        ),
    ]
