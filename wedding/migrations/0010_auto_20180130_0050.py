# Generated by Django 2.0.1 on 2018-01-30 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20180130_0044'),
        ('wedding', '0009_auto_20180117_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='wedding',
            name='bride',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bride_name', to='main_app.Person'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wedding',
            name='groom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='groom_name', to='main_app.Person'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wedding',
            name='minister',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='minister', to='main_app.Ministers'),
        ),
    ]
