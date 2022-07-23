from django.db import models
from django.urls import reverse

# Create your models here.

class Classis(models.Model):
    name = models.TextField('Название класса')
    info = models.TextField('Описание класса', blank=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('classis', kwargs={'classis_id': self.pk})

    class Meta:
        verbose_name = 'Класс животных'
        verbose_name_plural = 'Классы животных'
        ordering = ['name']

class Ordo(models.Model):
    name = models.TextField('Название отряда')
    info = models.TextField('Описание отряда', blank=True)
    classis = models.ForeignKey(Classis, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ordo', kwargs={'ordo_id': self.pk})

    class Meta:
        verbose_name = 'Отряд животных'
        verbose_name_plural = 'Отряды животных'
        ordering = ['name']