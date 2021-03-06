# Generated by Django 3.1.2 on 2020-11-30 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ImageSave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='hike',
            name='image',
        ),
        migrations.AddField(
            model_name='hike',
            name='image1',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='hike',
            name='image2',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='hike',
            name='image3',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='hike',
            name='tag',
            field=models.TextField(blank=True, default=''),
        ),
    ]
