from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title_post = models.CharField(max_length=255, verbose_name='Título')
    author_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    date_post = models.DateField(default=timezone.now, verbose_name='Título')
    content_post = models.TextField(verbose_name='Conteúdo')
    exerpt_post = models.TextField(verbose_name='Excerto')
    category_post = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria')
    image_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    pubished_post = models.BooleanField(default=False, verbose_name='Publicado')


    def __str__(self):
        return self.title_post