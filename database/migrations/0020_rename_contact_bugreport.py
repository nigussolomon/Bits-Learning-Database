# Generated by Django 4.0.1 on 2022-01-08 17:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0019_rename_email_contact_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='BugReport',
        ),
    ]
