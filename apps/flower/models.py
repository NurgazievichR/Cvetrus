from django.db import models

from apps.user.models import User

class Sort(models.Model):
    title = models.CharField('Название', max_length=15, unique=True)

    def __str__(self) -> str:
        return f'{self.title}'
    class Meta:
        verbose_name = 'Сорт'
        verbose_name_plural = 'Сорты'
        ordering = ('-id',)


class Plantation(models.Model):
    title = models.CharField('Название', max_length=15, unique=True)

    def __str__(self) -> str:
        return f'{self.title}'
    class Meta:
        verbose_name = 'Плантация'
        verbose_name_plural = 'Плантация'
        ordering = ('-id',)

class Flower(models.Model):
    COLORS = [
        ('Синий','Синий'),
        ('Красный','Красный'),
        ('Белый','Белый'),
        ('Голубой','Голубой'),
        ('Жёлтый','Жёлтый'),
        ('Чёрный','Чёрный'),
        ('Фиолетовый','Фиолетовый'),
    ]
    title = models.CharField('Название',max_length=15)
    image = models.ImageField('Фото', upload_to='media')
    sort = models.ForeignKey(Sort, on_delete=models.SET_NULL, null=True, verbose_name='Сорт')
    plantation = models.ForeignKey(Plantation, on_delete=models.SET_NULL, null=True, verbose_name='Плантация')
    length = models.CharField('Длина', max_length=15, choices=[(str(i),str(i)) for i in range(10, 101, 20)])
    color = models.CharField('Цвет', max_length=15, choices=COLORS)
    price = models.DecimalField('Цена',decimal_places=2, max_digits=10)
    views = models.PositiveBigIntegerField('Просмотры', default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_flowers', verbose_name='Владелец')

    def __str__(self) -> str:
        return f'{self.title}--{self.owner}--{self.id}'

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы'
        ordering = ('-id',)
