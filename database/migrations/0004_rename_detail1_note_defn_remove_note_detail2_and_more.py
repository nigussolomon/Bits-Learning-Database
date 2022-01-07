# Generated by Django 4.0 on 2021-12-30 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_rename_notes_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='detail1',
            new_name='defn',
        ),
        migrations.RemoveField(
            model_name='note',
            name='detail2',
        ),
        migrations.RemoveField(
            model_name='note',
            name='detail3',
        ),
        migrations.RemoveField(
            model_name='note',
            name='detail4',
        ),
        migrations.RemoveField(
            model_name='note',
            name='extra',
        ),
        migrations.RemoveField(
            model_name='note',
            name='intro1',
        ),
        migrations.RemoveField(
            model_name='note',
            name='intro2',
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
