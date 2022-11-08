from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    STATUS = [('1','Продавец'), ('2','Покупатель')]
    status = models.CharField('Статус',choices=STATUS, max_length=20, null=True, blank=True)
    photo = models.ImageField('Фото',blank=True, null=True, upload_to='images/')
    phone = models.CharField('Номер телефона',help_text="номер на WhatsApp, в международном формате", max_length=15, blank=True)
    email = models.EmailField('Email', blank=True)
    address = models.CharField('Адрес',max_length=100, blank=True)
    brief_description = models.CharField('Краткое описание', max_length=100, blank=True)
    last_activity = models.DateTimeField('Был в сети', default=timezone.now)

    def __str__(self) -> str:
        return f'{self.username}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)
