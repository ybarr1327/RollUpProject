# Generated by Django 3.1.7 on 2021-04-30 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0021_auto_20210430_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='participants',
            name='username',
            field=models.CharField(default='', max_length=100, verbose_name='username'),
        ),
    ]
