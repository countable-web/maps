# Generated by Django 2.2.8 on 2020-10-16 08:55

import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grant', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('language', models.CharField(blank=True, max_length=255, null=True)),
                ('recipient', models.TextField(blank=True, null=True)),
                ('community_affiliation', models.TextField(blank=True, null=True, verbose_name='Community/Affiliation')),
                ('title', models.TextField(blank=True, null=True)),
                ('project_brief', models.TextField(blank=True, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=100, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('province', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(default=None, null=True, srid=4326)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
            options={
                'ordering': ['grant'],
            },
        ),
    ]
