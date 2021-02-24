# Generated by Django 3.1.7 on 2021-02-24 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('variable', models.CharField(db_index=True, max_length=20, primary_key=True, serialize=False)),
                ('unit', models.CharField(max_length=20)),
                ('section', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WorldData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('scenario', models.CharField(db_index=True, max_length=50)),
                ('_2005', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2010', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2015', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2020', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2025', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2030', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2035', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2040', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2045', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2050', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2055', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2060', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2065', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2070', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2075', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2080', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2085', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2090', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2095', models.DecimalField(decimal_places=6, max_digits=12)),
                ('_2100', models.DecimalField(decimal_places=6, max_digits=12)),
                ('variable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.variable')),
            ],
            options={
                'verbose_name_plural': 'World Data',
                'unique_together': {('model', 'scenario', 'variable')},
            },
        ),
    ]
