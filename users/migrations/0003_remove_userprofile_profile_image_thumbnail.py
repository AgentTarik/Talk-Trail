# Generated by Django 5.0.7 on 2024-07-24 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_profile_image_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_image_thumbnail',
        ),
    ]