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


class Vacancy(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    language = models.ForeignKey('ProgrammingLanguage', on_delete=models.CASCADE, verbose_name='Язык программирования')
    url = models.URLField(unique=True)
    title = models.CharField(max_length=200, db_index=True, verbose_name='Заголовок вакансии')
    company = models.CharField(max_length=200, verbose_name='Компания')
    description = models.TextField('Описание вакансии')
    vacancy_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'

    def __str__(self):
        return self.title
