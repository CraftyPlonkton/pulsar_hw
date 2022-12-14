import os.path

from django.conf import settings
from django.db import models
from PIL import Image


class Item(models.Model):
    STATUSES = (
        ('AVAILABLE', 'В наличии'),
        ('ORDER', 'Под заказ'),
        ('AWAIT', 'Ожидается поступление'),
        ('UNAVAILABLE', 'Нет в наличии'),
        ('WITHDRAWN', 'Не производится')
    )
    name = models.CharField('Название', max_length=50)
    item_code = models.CharField('Артикул', max_length=50)
    price = models.FloatField('Цена')
    status = models.CharField('Статус', max_length=15, choices=STATUSES)
    image = models.ImageField('Изображение', upload_to='images')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_path_and_extension(self):
        path, ext = os.path.splitext(
            os.path.relpath(self.image.path, settings.BASE_DIR)
        )
        return path, ext

    def save(self):
        super().save()
        if self.image:
            path, ext = os.path.splitext(self.image.path)
            webp_image = Image.open(self.image)
            webp_image.save(path + '.webp', format='webp')

    def __str__(self):
        return self.name
