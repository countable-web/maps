# Generated by Django 2.2.8 on 2020-05-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0122_auto_20200530_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxonomy',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
