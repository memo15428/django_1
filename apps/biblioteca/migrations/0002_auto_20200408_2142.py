# Generated by Django 2.0.6 on 2020-04-09 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='nacionalidad',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
