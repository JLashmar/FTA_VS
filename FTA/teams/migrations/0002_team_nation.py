# Generated by Django 2.0.2 on 2018-02-19 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nations', '0001_initial'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='nation',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='nations.Country_Data'),
        ),
    ]
