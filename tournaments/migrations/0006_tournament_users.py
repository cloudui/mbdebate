# Generated by Django 2.2.7 on 2020-05-06 06:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournaments', '0005_auto_20200505_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
