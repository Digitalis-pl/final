from django.db import models

from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('document_detail', args=[str(self.id)])
