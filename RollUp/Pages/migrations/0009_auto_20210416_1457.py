# Generated by Django 3.1.7 on 2021-04-16 21:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0008_auto_20210416_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='num_signed_up',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(0)], verbose_name='size'))], verbose_name='num_signed_up'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='size',
            field=models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(0)], verbose_name='size'),
        ),
    ]
