# Generated by Django 4.1.3 on 2022-11-08 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название сайта')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Логотип')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Описание сайта')),
                ('phone', models.CharField(blank=True, help_text='номер на WhatsApp, в международном формате', max_length=15, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('instagram', models.CharField(blank=True, help_text='ссылка на instagram', max_length=50, verbose_name='Instagram')),
                ('twitter', models.CharField(blank=True, help_text='ссылка на twitter', max_length=50, verbose_name='Twitter')),
                ('telegram', models.CharField(blank=True, help_text='ссылка на telegram', max_length=50, verbose_name='Telegram')),
                ('vkontakte', models.CharField(blank=True, help_text='ссылка на ВКонтакте', max_length=50, verbose_name='ВКонтакте')),
            ],
            options={
                'verbose_name': 'Настройки',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]