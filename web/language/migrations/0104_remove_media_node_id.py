# Generated by Django 2.2.8 on 2020-03-18 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0103_auto_20200318_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='node_id',
        ),
    ]