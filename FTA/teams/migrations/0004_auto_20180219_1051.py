# Generated by Django 2.0.2 on 2018-02-19 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20180219_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='gender',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Mixed', 'Mixed')], default='Men', max_length=5),
        ),
        migrations.AlterField(
            model_name='team',
            name='tier',
            field=models.CharField(choices=[('International', 'International'), ('Domestic', 'Domestic')], default='Men', max_length=13),
        ),
    ]
