# Generated by Django 2.0.2 on 2018-02-19 13:24

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20180206_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='church',
            name='banns_current_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20),
        ),
        migrations.AddField(
            model_name='church',
            name='banns_upcoming_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='banns_upcoming_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20),
        ),
        migrations.AddField(
            model_name='church',
            name='statutory_current_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20),
        ),
        migrations.AddField(
            model_name='church',
            name='statutory_upcoming_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='church',
            name='statutory_upcoming_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=20),
        ),
    ]
