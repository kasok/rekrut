# Generated by Django 2.0.1 on 2018-01-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_messages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='read_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
