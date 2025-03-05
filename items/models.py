from django.db import models


class Item(models.Model):
    """Элемент выбора для голосования."""
    image = models.ImageField(verbose_name='Изображение', upload_to="images/", blank=True)
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    description = models.TextField(max_length=1000, verbose_name='Описание', blank=True, null=True)
    counter = models.PositiveIntegerField(verbose_name='Голосов', default=0)

    def __str__(self):
        return self.title