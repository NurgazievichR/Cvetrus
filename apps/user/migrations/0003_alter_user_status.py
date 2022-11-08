# Generated by Django 4.1.3 on 2022-11-08 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('1', 'Продавец'), ('2', 'Покупатель')], max_length=20, null=True, verbose_name='Статус'),
        ),
    ]
