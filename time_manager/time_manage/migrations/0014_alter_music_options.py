# Generated by Django 4.0.3 on 2022-04-16 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('time_manage', '0013_alter_music_music_conductor_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='music',
            options={'ordering': ['id', 'music_composer', 'music_title'], 'verbose_name': '곡 정보', 'verbose_name_plural': '곡 정보'},
        ),
    ]