# Generated by Django 2.2.7 on 2020-05-10 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200509_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
