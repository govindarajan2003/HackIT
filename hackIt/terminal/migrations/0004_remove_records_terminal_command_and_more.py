# Generated by Django 4.1.13 on 2024-03-16 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0003_alter_records_terminal_command_alter_records_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='records',
            name='terminal_command',
        ),
        migrations.RemoveField(
            model_name='records',
            name='user_id',
        ),
    ]
