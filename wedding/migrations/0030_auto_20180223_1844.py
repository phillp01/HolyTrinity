# Generated by Django 2.0.2 on 2018-02-23 13:14

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0029_auto_20180223_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='wedding',
            name='bells_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20),
        ),
        migrations.AddField(
            model_name='wedding',
            name='car_park_attendant_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20),
        ),
        migrations.AddField(
            model_name='wedding',
            name='cd_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20),
        ),
        migrations.AddField(
            model_name='wedding',
            name='choir_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20),
        ),
        migrations.AddField(
            model_name='wedding',
            name='flowers_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20),
        ),
        migrations.AddField(
            model_name='wedding',
            name='organ_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20),
        ),
        migrations.AddField(
            model_name='wedding',
            name='verger_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20),
        ),
        migrations.AddField(
            model_name='wedding',
            name='video_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20),
        ),
        migrations.AddField(
            model_name='wedding',
            name='winter_heating_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='banns_no',
            field=models.CharField(blank=True, default=False, max_length=50, null=True),
        ),
    ]
