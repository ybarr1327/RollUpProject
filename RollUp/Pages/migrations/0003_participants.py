# Generated by Django 3.1.7 on 2021-04-09 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0002_delete_participants'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('participant_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='participant_id')),
                ('email', models.CharField(max_length=50, verbose_name='email')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Pages.classes')),
            ],
        ),
    ]
