from django.db import models
from django.urls import reverse

# Create your models here.

class Classis(models.Model):
    name = models.TextField('Название класса')
    info = models.TextField('Описание класса', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url_classis1(self):
        return reverse('classis_post', kwargs={'classis_post_id': self.pk})

    def get_absolute_url_classis2(self):
        return reverse('sidebar_classis_list', kwargs={'classis_list_id': self.pk})

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

    def get_absolute_url_ordo1(self):
        return reverse('ordo_post', kwargs={'ordo_post_id': self.pk, 'classis_id': self.classis.id})

    def get_absolute_url_ordo2(self):
        return reverse('sidebar_ordo_list', kwargs={'ordo_list_id': self.pk, 'classis_id': self.classis.id})

    class Meta:
        verbose_name = 'Отряд животных'
        verbose_name_plural = 'Отряды животных'
        ordering = ['name']

class Familia(models.Model):
    name = models.TextField('Название семейства')
    info = models.TextField('Описание семейства', blank=True)
    ordo = models.ForeignKey(Ordo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url_familia1(self):
        return reverse('familia_post', kwargs={'familia_post_id': self.pk, 'classis_id': self.ordo.id, 'ordo_id': self.ordo.id})

    def get_absolute_url_familia2(self):
        return reverse('sidebar_familia_list', kwargs={'familia_list_id': self.pk, 'classis_id': self.ordo.id, 'ordo_id': self.ordo.id})

    class Meta:
        verbose_name = 'Семейство животных'
        verbose_name_plural = 'Семейства животных'
        ordering = ['name']

class Genus(models.Model):
    name = models.TextField('Название рода')
    info = models.TextField('Описание рода', blank=True)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url_genus1(self):
        return reverse('genus_post', kwargs={'genus_post_id': self.pk, 'classis_id': self.familia.id, 'ordo_id': self.familia.id, 'familia_id': self.familia.id})

    def get_absolute_url_genus2(self):
        return reverse('sidebar_genus_list', kwargs={'genus_list_id': self.pk, 'classis_id': self.familia.id, 'ordo_id': self.familia.id, 'familia_id': self.familia.id})

    class Meta:
        verbose_name = 'Род животных'
        verbose_name_plural = 'Роды животных'
        ordering = ['name']

class Species(models.Model):
    name = models.TextField('Название вида')
    info = models.TextField('Описание вида', blank=True)
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url_species1(self):
        return reverse('species_post', kwargs={'species_post_id': self.pk, 'classis_id': self.genus.id, 'ordo_id': self.genus.id,'familia_id': self.genus.id, 'genus_id': self.genus.id})

    class Meta:
        verbose_name = 'Вид животных'
        verbose_name_plural = 'Виды животных'
        ordering = ['name']