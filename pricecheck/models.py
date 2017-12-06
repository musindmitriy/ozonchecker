from django.db import models

# Create your models here.

class Item(models.Model):

    name = models.CharField(verbose_name="Название товара", max_length=500)
    link = models.URLField(verbose_name="Ссылка на товар", unique=True)

    def __str__(self):
        return self.name


class Price(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Дата снятия цены", auto_now_add=True)
    price = models.PositiveIntegerField(verbose_name="Цена в рублях")  # Опустим копейки

    class Meta:
        unique_together = ("item", "date")
        # В один день мы снимаем цену только 1 раз
