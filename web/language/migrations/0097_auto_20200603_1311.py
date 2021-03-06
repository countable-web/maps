# Generated by Django 2.2.8 on 2020-06-03 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0096_auto_20191230_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='community',
            name='nation_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='community',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='medias', to='language.Community'),
        ),
        migrations.AlterField(
            model_name='media',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='media',
            name='placename',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='medias', to='language.PlaceName'),
        ),
        migrations.AlterField(
            model_name='media',
            name='url',
            field=models.URLField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
