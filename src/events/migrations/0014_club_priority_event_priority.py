# Generated by Django 4.2.3 on 2023-08-01 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_rename_location_event_location_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='priority',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='event',
            name='priority',
            field=models.IntegerField(default=1),
        ),
    ]
