# Generated by Django 2.0.1 on 2018-02-06 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20180130_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='wedding_id',
            field=models.IntegerField(blank=True, default=1, max_length=5),
            preserve_default=False,
        ),
    ]
