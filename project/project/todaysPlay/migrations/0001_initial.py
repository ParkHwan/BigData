# Generated by Django 4.0.2 on 2022-03-06 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stationName', models.CharField(max_length=30)),
                ('lat', models.IntegerField()),
                ('lng', models.IntegerField()),
                ('hosun', models.CharField(max_length=15)),
            ],
        ),
    ]