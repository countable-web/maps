# Generated by Django 2.2.3 on 2019-07-05 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0007_community_english_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='internet_speed',
            field=models.CharField(default='', max_length=255),
        ),
    ]
