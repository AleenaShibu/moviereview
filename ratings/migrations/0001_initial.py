# Generated by Django 2.2.5 on 2019-09-23 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=50)),
                ('release_year', models.CharField(max_length=4)),
                ('director', models.CharField(max_length=30)),
                ('review', models.TextField()),
                ('rating', models.CharField(choices=[('1', '*'), ('2', '**'), ('3', '***'), ('4', '****'), ('5', '*****')], default='1', max_length=2)),
            ],
        ),
    ]
