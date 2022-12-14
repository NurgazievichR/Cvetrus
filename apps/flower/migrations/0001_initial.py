# Generated by Django 4.1.3 on 2022-11-08 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plantation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Плантация',
                'verbose_name_plural': 'Плантация',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Sort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Сорт',
                'verbose_name_plural': 'Сорты',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, verbose_name='Название')),
                ('image', models.ImageField(upload_to='media', verbose_name='Фото')),
                ('length', models.CharField(choices=[('10', '10'), ('30', '30'), ('50', '50'), ('70', '70'), ('90', '90')], max_length=15, verbose_name='Длина')),
                ('color', models.CharField(choices=[('Синий', 'Синий'), ('Красный', 'Красный'), ('Белый', 'Белый'), ('Голубой', 'Голубой'), ('Жёлтый', 'Жёлтый'), ('Чёрный', 'Чёрный'), ('Фиолетовый', 'Фиолетовый')], max_length=15, verbose_name='Цвет')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('views', models.PositiveBigIntegerField(verbose_name='Просмотры')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_flowers', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
                ('plantation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flower.plantation', verbose_name='Плантация')),
                ('sort', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flower.sort', verbose_name='Сорт')),
            ],
            options={
                'verbose_name': 'Цветок',
                'verbose_name_plural': 'Цветы',
                'ordering': ('-id',),
            },
        ),
    ]
