from django.db import models

from users.models import User


class MyAllergy(models.Model):
    name = models.CharField(
            verbose_name='Название',
            max_length=100
        )
    user_products = models.ManyToManyField(
            'Product',
            blank=True,
            related_name='products',
            verbose_name='Продукт питания Моей Аллергии'
        )
    user_animals = models.ManyToManyField(
            'Animal',
            blank=True,
            related_name='animals',
            verbose_name='Животные Моей Аллергии'
        )
    user_plants = models.ManyToManyField(
            'Plant',
            blank=True,
            related_name='plants',
            verbose_name='Растения содержащие Аллерген'
        )
    user = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name='user',
            verbose_name='Пользователь'
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Моя Аллергия'
        verbose_name_plural = 'Мои Аллергии'


class Product(models.Model):
    name = models.CharField(
            verbose_name='Название',
            max_length=100
        )
    description = models.CharField(
            verbose_name='Описание',
            max_length=500
        )
    allergens = models.ManyToManyField(
            'Allergen',
            verbose_name='Аллергены'
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт питания'
        verbose_name_plural = 'Продукты питания'


class Animal(models.Model):
    name = models.CharField(
            max_length=100,
            verbose_name='Название'
        )
    description = models.CharField(
            max_length=500,
            verbose_name='Описание'
        )
    allergens = models.ManyToManyField(
            'Allergen',
            verbose_name='Аллергены'
        )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Животное содержащее Аллерген'
        verbose_name_plural = 'Животные содержащие Аллерген'


class Plant(models.Model):
    name = models.CharField(
            max_length=100,
            verbose_name='Название'
        )
    description = models.CharField(
            max_length=500,
            verbose_name='Описание'
        )
    allergens = models.ManyToManyField(
            'Allergen',
            verbose_name='Аллергены'
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'

    
class Allergen(models.Model):
    name = models.CharField(
            max_length=100,
            verbose_name='Название'
        )
    description = models.CharField(
            max_length=500,
            verbose_name='Описание'
        )

    class Meta:
        verbose_name = 'Аллерген'
        verbose_name_plural = 'Аллергены'

    def __str__(self):
        return self.name
