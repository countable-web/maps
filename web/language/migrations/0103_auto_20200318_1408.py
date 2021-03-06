# Generated by Django 2.2.8 on 2020-03-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0102_placename_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placename',
            name='details',
        ),
        migrations.RemoveField(
            model_name='placename',
            name='is_art',
        ),
        migrations.RemoveField(
            model_name='placename',
            name='node_id',
        ),
        migrations.RemoveField(
            model_name='placename',
            name='node_type',
        ),
        migrations.AlterField(
            model_name='placename',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='placename',
            name='kind',
            field=models.CharField(default='', max_length=20),
        ),
    ]
