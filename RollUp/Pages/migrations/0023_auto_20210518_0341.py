# Generated by Django 3.1.7 on 2021-05-18 10:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0022_participants_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='num_signed_up',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='num_signed_up'),
        ),
    ]
