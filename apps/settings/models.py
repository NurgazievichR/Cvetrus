from django.db import models

class Setting(models.Model):
    title = models.CharField('Название сайта',max_length=20)
    logo = models.ImageField('Логотип',blank=True, null=True, upload_to='images/')
    description = models.CharField(verbose_name="Описание сайта",max_length=255, blank=True)
    phone = models.CharField('Номер телефона',help_text="номер на WhatsApp, в международном формате", max_length=15, blank=True)
    email = models.EmailField('Email', blank=True)
    instagram = models.CharField('Instagram',help_text="ссылка на instagram", blank=True,max_length=50)
    twitter = models.CharField('Twitter',help_text="ссылка на twitter", blank=True,max_length=50)
    telegram = models.CharField('Telegram',help_text="ссылка на telegram", blank=True, max_length=50)
    vkontakte = models.CharField('ВКонтакте',help_text="ссылка на ВКонтакте", blank=True, max_length=50)

    def __str__(self):
        return f"ID: {self.id} ||||| {self.title}"

    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'