# Generated by Django 2.0.2 on 2018-02-19 13:04

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0015_extraprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extraprice',
            name='Choir',
        ),
        migrations.RemoveField(
            model_name='extraprice',
            name='Organ',
        ),
        migrations.RemoveField(
            model_name='extraprice',
            name='bells',
        ),
        migrations.RemoveField(
            model_name='extraprice',
            name='bylicense',
        ),
        migrations.RemoveField(
            model_name='extraprice',
            name='carParkAttendant',
        ),
        migrations.RemoveField(
            model_name='extraprice',
            name='cd',
        ),
        migrations.RemoveField(
            model_name='extraprice',
            name='flowers',
        ),
        migrations.RemoveField(
            model_name='extraprice',
            name='verger',
        ),
        migrations.RemoveField(
            model_name='extraprice',
            name='video',
        ),
        migrations.RemoveField(
            model_name='extraprice',
            name='winterHeating',
        ),
        migrations.AddField(
            model_name='extraprice',
            name='name',
            field=models.CharField(choices=[('CONTINUING_EDUCATION_STUDIES', 'Continuing Education studies'), ('TECHNIQUE', 'Technique')], default=Decimal('0.0000'), max_length=100, verbose_name='nombre'),
        ),
    ]