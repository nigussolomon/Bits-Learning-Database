# Generated by Django 4.0.1 on 2022-01-07 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
