from django.db import models
from django.utils import timezone

from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Оглавление')
    description = models.TextField(verbose_name='Описание')
    rubrics = models.CharField(max_length=255, verbose_name='Рубрика')
    created_date = models.DateField(max_length=255, verbose_name='Дата создания', default=timezone.now)
    text = models.TextField(verbose_name='Текст статьи')

    def __str__(self):
        return f'{self.title} {self.rubrics} {self.created_date}'

    def get_absolute_url(self):
        return reverse('document_detail', args=[str(self.id)])
