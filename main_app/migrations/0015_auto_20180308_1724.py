# Generated by Django 2.0.2 on 2018-03-08 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_auto_20180223_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.CharField(blank=True, choices=[('Single', 'Sinlge'), ('PMD', 'Previous Marriage Dissolved'), ('Widowed', 'Widowed'), ('CPD', 'Civil Partnership Dissolved')], max_length=150),
        ),
    ]
