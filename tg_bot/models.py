from django.db import models


class TypeOfLocality(models.TextChoices):
    citi = 'Город'
    pgt = 'Поселок городского типа'


class Locality(models.Model):
    title = models.CharField('Наименование', max_length=30, unique=True)
    href = models.CharField('Ссылка', max_length=120)
    population = models.IntegerField('Население')
    type = models.CharField(
        'Тип населенного пункта', max_length=24, choices=TypeOfLocality.choices
    )
