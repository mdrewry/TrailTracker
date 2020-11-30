# Generated by Django 3.1.2 on 2020-11-30 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_delete_togglevar'),
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
        migrations.AlterField(
            model_name='hike',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
