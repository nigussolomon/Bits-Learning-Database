# Generated by Django 4.0.1 on 2022-01-08 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0020_rename_contact_bugreport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bugreport',
            old_name='title',
            new_name='bug',
        ),
        migrations.RenameField(
            model_name='bugreport',
            old_name='message',
            new_name='bug_detail',
        ),
    ]
