# Generated by Django 4.1.13 on 2024-03-17 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0012_records_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='status',
            field=models.CharField(choices=[(1, 'SCHEDULED'), (2, 'IN PROGRESS'), (3, 'COMPLETED'), (4, 'TEST ERROR')], default=(1, 'SCHEDULED'), max_length=50),
        ),
    ]