# Generated by Django 4.0.3 on 2022-04-11 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('time_manage', '0007_rename__time_unique_id_timeinfo_time_unique_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timeinfo',
            options={'ordering': ['time_date', 'time_start'], 'verbose_name': '타임 정보', 'verbose_name_plural': '타임 정보'},
        ),
        migrations.RenameField(
            model_name='music',
            old_name='_composer',
            new_name='music_composer',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='_conductor',
            new_name='music_conductor',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='_orchestra',
            new_name='music_orchestra',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='_title',
            new_name='music_title',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='_time_info',
            new_name='time_info',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='_music',
            new_name='music',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='_player',
            new_name='player',
        ),
        migrations.RenameField(
            model_name='timeinfo',
            old_name='_time_date',
            new_name='time_date',
        ),
        migrations.RenameField(
            model_name='timeinfo',
            old_name='_time_end',
            new_name='time_end',
        ),
        migrations.RenameField(
            model_name='timeinfo',
            old_name='_time_manager',
            new_name='time_manager',
        ),
        migrations.RenameField(
            model_name='timeinfo',
            old_name='_time_start',
            new_name='time_start',
        ),
    ]