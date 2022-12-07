from django.db import models

from users.models import User


class MyAllergy(models.Model):
    name = models.CharField(
            max_length=100,
            verbose_name='Название'
        )
    carriers = models.ManyToManyField(
            'Carrier',
            verbose_name='Носители'
        )
    user = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            verbose_name='Пользователь'
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Моя Аллергия'
        verbose_name_plural = 'Карточки Аллергии'


class Category(models.Model):
    name = models.CharField(
            max_length=100,
            verbose_name='Название'
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Категория'
        verbose_name_plural = 'Категории'


class Carrier(models.Model):
    name = models.CharField(
            max_length=100,
            verbose_name='Название'
        )
    image = models.ImageField(
            upload_to='carriers',
            verbose_name='Фото'
        )
    description = models.CharField(
            max_length=1000,
            verbose_name='Описание'
        )
    category = models.ForeignKey(
            'Category',
            on_delete=models.DO_NOTHING,
            verbose_name='Категория',
            related_name='carriers'
        )
    allergen = models.ForeignKey(
            'Allergen',
            on_delete=models.DO_NOTHING,
            verbose_name='Аллерген',
            related_name='allergens'
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Носитель'
        verbose_name_plural='Носители'


class Allergen(models.Model):
    name = models.CharField(
            max_length=100,
            verbose_name='Аллерген'
        )
    description = models.CharField(
            max_length=1000,
            verbose_name='Описание'
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Аллерген'
        verbose_name_plural = 'Аллергены'
