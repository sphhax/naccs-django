# Generated by Django 2.2.4 on 2019-10-23 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0005_auto_20191023_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='division',
            name='fee',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='division',
            name='sub_fee',
            field=models.FloatField(default=0),
        ),
    ]