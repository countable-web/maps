# Generated by Django 2.2.8 on 2020-07-14 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0132_auto_20200709_1746'),
        ('users', '0016_user_non_bc_languages'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='artist_profile',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='language.PlaceName'),
        ),
    ]
