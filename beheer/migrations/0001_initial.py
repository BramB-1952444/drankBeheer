# Generated by Django 3.1.5 on 2021-01-04 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PrijsKlasse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('normaal', models.DecimalField(decimal_places=2, max_digits=6)),
                ('zwaar', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Telling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aantalNormaal', models.IntegerField()),
                ('aantalZwaar', models.IntegerField()),
                ('leider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beheer.leider')),
                ('prijsKlasse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='beheer.prijsklasse')),
            ],
        ),
        migrations.CreateModel(
            name='Betaling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Leider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beheer.leider')),
            ],
        ),
    ]