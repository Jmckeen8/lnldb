# Generated by Django 3.1.3 on 2023-09-06 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0011_auto_20230905_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configurationprofile',
            name='profile',
            field=models.FilePathField(match='.*\\.json$', path='/home/lnl/public_html/media/profiles'),
        ),
    ]
