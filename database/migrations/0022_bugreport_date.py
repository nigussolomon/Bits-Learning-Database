# Generated by Django 4.0.1 on 2022-01-08 20:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0021_rename_title_bugreport_bug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugreport',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]