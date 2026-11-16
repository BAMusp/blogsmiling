from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.pk])


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(default=timezone.now)
    categorias = models.ManyToManyField(Category, related_name='posts', blank=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField()
    data_postagem = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-data_postagem']

    def __str__(self):
        return f'{self.autor} em "{self.post}"'