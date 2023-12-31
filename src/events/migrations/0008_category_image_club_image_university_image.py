# Generated by Django 4.2.3 on 2023-07-27 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/categories/'),
        ),
        migrations.AddField(
            model_name='club',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/clubs/'),
        ),
        migrations.AddField(
            model_name='university',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/universities/'),
        ),
    ]
