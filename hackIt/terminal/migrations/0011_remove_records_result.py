# Generated by Django 4.1.13 on 2024-03-17 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0010_alter_records_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='records',
            name='result',
        ),
    ]
