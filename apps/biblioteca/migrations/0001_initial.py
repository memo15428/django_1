# Generated by Django 2.0.6 on 2020-04-08 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, verbose_name='Nombres')),
                ('nacionalidad', models.CharField(blank=True, max_length=100, verbose_name='Nacionalidad')),
            ],
        ),
    ]