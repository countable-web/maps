# Generated by Django 2.2.4 on 2019-08-25 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('language', '0058_auto_20190825_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediafavourite',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
