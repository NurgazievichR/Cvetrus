# Generated by Django 4.1.3 on 2022-11-08 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantation',
            name='title',
            field=models.CharField(max_length=15, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='sort',
            name='title',
            field=models.CharField(max_length=15, unique=True, verbose_name='Название'),
        ),
    ]