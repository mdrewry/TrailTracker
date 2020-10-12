# Generated by Django 3.1.1 on 2020-10-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miles', models.FloatField(blank=True, null=True)),
                ('elevationGain', models.FloatField()),
                ('elevationLoss', models.FloatField(blank=True, null=True)),
                ('description', models.TextField()),
                ('starred', models.BooleanField()),
            ],
        ),
    ]
