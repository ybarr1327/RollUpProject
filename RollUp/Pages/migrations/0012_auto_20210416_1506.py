# Generated by Django 3.1.7 on 2021-04-16 22:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0011_auto_20210416_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='classes',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
