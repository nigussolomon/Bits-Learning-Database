# Generated by Django 4.0.1 on 2022-01-07 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_test_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='user',
            new_name='author',
        ),
    ]
