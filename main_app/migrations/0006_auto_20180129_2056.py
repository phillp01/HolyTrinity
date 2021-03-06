# Generated by Django 2.0.1 on 2018-01-29 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_person_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proofs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proof', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='qualifyingConnections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualifying_connection', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='connected_by_marriage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='details',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='person',
            name='dob',
            field=models.DateField(blank=True, default='2018-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='father_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='person',
            name='father_occupation',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='person',
            name='if_yes_how',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='person',
            name='nationality',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='person',
            name='occupation',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AddField(
            model_name='person',
            name='status',
            field=models.CharField(blank=True, choices=[('Single', 'Sinlge'), ('PMD', 'Previous Marriage Dissolved'), ('Widowed', 'Widowed'), ('CPD', 'Civil Partnership Dissolved')], max_length=3),
        ),
        migrations.AlterField(
            model_name='person',
            name='church',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='church', to='main_app.Church'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='role', to='main_app.Role'),
        ),
        migrations.AddField(
            model_name='person',
            name='proof',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, related_name='proofOfId', to='main_app.Proofs'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='qualifying_connection',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, related_name='qualConnect', to='main_app.qualifyingConnections'),
            preserve_default=False,
        ),
    ]
