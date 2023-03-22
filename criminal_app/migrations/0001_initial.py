# Generated by Django 4.1.7 on 2023-03-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('criminal_number', models.TextField(blank=True)),
                ('nickname', models.TextField(blank=True)),
                ('address', models.TextField(blank=True)),
                ('date_of_crime', models.TextField(blank=True)),
                ('arrest_date', models.TextField(blank=True)),
                ('occupation', models.TextField(blank=True)),
                ('crime_type', models.TextField(blank=True)),
                ('age', models.TextField(blank=True)),
                ('fathers_name', models.TextField(blank=True)),
                ('gender', models.TextField(blank=True)),
                ('wanted', models.TextField(blank=True)),
                ('criminal_image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
    ]
