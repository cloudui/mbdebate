# Generated by Django 2.2.7 on 2020-05-05 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0004_auto_20200505_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='link',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
