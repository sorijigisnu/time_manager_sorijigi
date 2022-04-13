# Generated by Django 4.0.3 on 2022-04-11 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_manage', '0008_alter_timeinfo_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timeinfo',
            options={'ordering': ['-time_date', '-time_start'], 'verbose_name': '타임 정보', 'verbose_name_plural': '타임 정보'},
        ),
        migrations.AlterField(
            model_name='music',
            name='music_conductor',
            field=models.CharField(blank=True, default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='music',
            name='music_orchestra',
            field=models.CharField(blank=True, default='None', max_length=200),
        ),
    ]