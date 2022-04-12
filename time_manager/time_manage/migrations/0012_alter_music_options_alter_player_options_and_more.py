# Generated by Django 4.0.3 on 2022-04-12 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('time_manage', '0011_alter_music_music_conductor_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='music',
            options={'ordering': ['music_composer', 'music_title'], 'verbose_name': '곡 정보', 'verbose_name_plural': '곡 정보'},
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['player_name'], 'verbose_name': '연주자', 'verbose_name_plural': '연주자'},
        ),
        migrations.RenameField(
            model_name='player',
            old_name='player',
            new_name='player_name',
        ),
    ]
