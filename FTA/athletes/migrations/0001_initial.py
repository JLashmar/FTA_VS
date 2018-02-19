# Generated by Django 2.0.2 on 2018-02-19 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nations', '0002_remove_country_data_sport'),
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('initials', models.CharField(max_length=10)),
                ('nationality', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='nations.Country_Data')),
                ('sport', models.ManyToManyField(to='sports.Sport')),
            ],
        ),
    ]
