# Generated by Django 3.2 on 2021-04-21 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0016_auto_20210421_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='participants',
            name='class_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='Pages.classes'),
        ),
    ]