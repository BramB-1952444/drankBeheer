# Generated by Django 3.1.5 on 2021-01-06 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beheer', '0007_auto_20210106_1908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leider',
            options={'ordering': ['volgorde']},
        ),
        migrations.AlterField(
            model_name='telling',
            name='aantalNormaal',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='telling',
            name='aantalZwaar',
            field=models.IntegerField(default=0, null=True),
        ),
    ]