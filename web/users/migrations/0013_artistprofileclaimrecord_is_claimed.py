# Generated by Django 2.2.8 on 2020-04-24 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_artistprofileclaimrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistprofileclaimrecord',
            name='is_claimed',
            field=models.BooleanField(default=False),
        ),
    ]
