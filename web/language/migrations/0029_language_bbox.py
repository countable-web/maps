# Generated by Django 2.2.3 on 2019-07-16 19:28

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0028_lna_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='bbox',
            field=django.contrib.gis.db.models.fields.PolygonField(default=None, null=True, srid=4326),
        ),
    ]
