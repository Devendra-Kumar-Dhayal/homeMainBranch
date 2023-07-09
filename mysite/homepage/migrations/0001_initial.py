# Generated by Django 4.2.2 on 2023-07-08 20:31

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameInfo',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='demo', max_length=343)),
                ('required_age', models.IntegerField(default=0)),
                ('is_free', models.BooleanField(default=False)),
                ('controller_support', models.CharField(default='demo')),
                ('dlc', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None)),
                ('detailed_description', models.CharField(default='demo', max_length=2000)),
                ('about_the_game', models.CharField(default='demo', max_length=2000)),
                ('short_description', models.CharField(default='demo', max_length=2000)),
                ('supported_languages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=list, size=None)),
                ('header_image', models.ImageField(default='default.jpg', upload_to='')),
                ('capsule_image', models.ImageField(default='default.jpg', upload_to='')),
                ('capsule_imagev5', models.ImageField(default='default.jpg', upload_to='')),
                ('website', models.URLField(default='demo')),
                ('pc_minimum', models.CharField(default='demo', max_length=500)),
                ('pc_recommended', models.CharField(default='demo', max_length=500)),
                ('mac_requirements', models.CharField(default='demo', max_length=500)),
                ('mac_recommended', models.CharField(default='demo', max_length=500)),
                ('linux_requirements', models.CharField(default='demo', max_length=500)),
                ('linux_recommended', models.CharField(default='demo', max_length=500)),
                ('developers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=list, size=None)),
                ('publishers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=list, size=None)),
                ('windows', models.BooleanField(default=False)),
                ('mac', models.BooleanField(default=False)),
                ('linux', models.BooleanField(default=False)),
                ('metacritic', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('screenshots', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('movies', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('recommendations', models.IntegerField(default=0)),
                ('coming_soon', models.BooleanField(default=False)),
                ('release_date', models.CharField(default='demo')),
                ('support_url', models.CharField(default='demo')),
                ('support_email', models.CharField(default='demo')),
                ('background', models.ImageField(default='default.jgp', upload_to='')),
                ('background_raw', models.ImageField(default='default.jpg', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='GameGenre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(default='demo', max_length=100)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.gameinfo')),
            ],
        ),
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(default='demo', max_length=100)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.gameinfo')),
            ],
        ),
    ]
