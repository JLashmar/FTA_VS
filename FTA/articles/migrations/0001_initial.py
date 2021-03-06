# Generated by Django 2.0.2 on 2018-02-19 02:56

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sports', '0001_initial'),
        ('teams', '0002_team_nation'),
        ('nations', '0002_remove_country_data_sport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('post_slug', models.SlugField(max_length=100, unique=True)),
                ('short_description', models.CharField(blank=True, max_length=150, null=True)),
                ('body', models.TextField()),
                ('headline_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('youtube_link', models.URLField(blank=True, null=True)),
                ('posted', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('country_slug', models.ManyToManyField(related_name='nation_slug', to='nations.Country_Data')),
                ('post_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_category', to='sports.Sport')),
                ('team_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_team', to='teams.Team')),
                ('team_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_team', to='teams.Team')),
            ],
        ),
        migrations.CreateModel(
            name='VideoNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('link', models.URLField()),
                ('video', embed_video.fields.EmbedVideoField()),
                ('posted', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('related_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Post')),
            ],
        ),
    ]
