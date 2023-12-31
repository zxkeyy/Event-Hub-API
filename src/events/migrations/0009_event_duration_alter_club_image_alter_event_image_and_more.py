# Generated by Django 4.2.3 on 2023-07-27 11:59

from django.db import migrations, models
import events.validators


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_category_image_club_image_university_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='duration',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='club',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/clubs/', validators=[events.validators.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/events/', validators=[events.validators.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='university',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/universities/', validators=[events.validators.validate_file_size]),
        ),
    ]
