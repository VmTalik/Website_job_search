from django.db import models
from .utilities import translation_slag


class City(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Название города', unique=True)
    slug = models.CharField(max_length=30, blank=True, unique=True)

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translation_slag(str(self.name))
        super().save(*args, **kwargs)


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Язык программирования', unique=True)
    slug = models.CharField(max_length=30, blank=True, unique=True)

    class Meta:
        verbose_name = 'язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translation_slag(str(self.name))
        super().save(*args, **kwargs)
