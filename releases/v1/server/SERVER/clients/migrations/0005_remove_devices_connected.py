# Generated by Django 2.0 on 2018-05-21 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_devices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devices',
            name='connected',
        ),
    ]