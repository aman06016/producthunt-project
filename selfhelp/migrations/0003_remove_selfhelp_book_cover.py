# Generated by Django 2.2 on 2020-05-04 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selfhelp', '0002_remove_selfhelp_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selfhelp',
            name='Book_cover',
        ),
    ]
