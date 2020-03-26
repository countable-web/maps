# Generated by Django 2.2.8 on 2020-03-25 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0109_placename_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='placename',
            name='public_arts',
            field=models.ManyToManyField(through='language.PublicArtArtist', to='language.PlaceName'),
        ),
    ]