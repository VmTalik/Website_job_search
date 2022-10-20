from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Название города', unique=True)
    slug = models.CharField(max_length=30, blank=True, unique=True)

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Язык программирования', unique=True)
    slug = models.CharField(max_length=30, blank=True, unique=True)

    class Meta:
        verbose_name = 'язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name
