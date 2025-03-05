from django.db import models


class Item(models.Model):
    """Элемент выбора для голосования."""
    image = models.ImageField(verbose_name='Изображение', upload_to="images/", blank=True)
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    description = models.TextField(max_length=1000, verbose_name='Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Элемент голосования'
        verbose_name_plural = 'Элементы голосования'

    def __str__(self):
        return self.title

    def count_votes(self):
        return self.vote_set.count()


class Vote(models.Model):
    """Голос."""
    ip = models.GenericIPAddressField(protocol='IPv4')
    choice = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Выбор')
