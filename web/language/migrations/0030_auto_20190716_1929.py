# Generated by Django 2.2.3 on 2019-07-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0029_language_bbox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='color',
            field=models.CharField(max_length=15),
        ),
    ]
