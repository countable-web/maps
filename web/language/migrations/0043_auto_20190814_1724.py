# Generated by Django 2.2.4 on 2019-08-14 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0042_auto_20190812_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='placename',
            name='community_only',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='placename',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='placename',
            name='traditional_name',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='placename',
            name='western_name',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('file_type', models.CharField(default=None, max_length=16)),
                ('url', models.CharField(default=None, max_length=255, null=True)),
                ('media_file', models.FileField(blank=True, null=True, upload_to='')),
                ('placename', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='language.PlaceName')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommunityLanguageStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='language.Community')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='language.Language')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]
