# Generated by Django 2.0.2 on 2018-02-19 13:46

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0017_auto_20180219_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalservices',
            name='name',
            field=models.CharField(choices=[('CONTINUING_EDUCATION_STUDIES', 'Continuing Education studies'), ('TECHNIQUE', 'Technique')], default=Decimal('0.0000'), max_length=100, verbose_name='nombre'),
        ),
    ]