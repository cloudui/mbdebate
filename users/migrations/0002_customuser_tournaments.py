# Generated by Django 2.2.7 on 2020-05-06 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0005_auto_20200505_1505'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='tournaments',
            field=models.ManyToManyField(to='tournaments.Tournament'),
        ),
    ]