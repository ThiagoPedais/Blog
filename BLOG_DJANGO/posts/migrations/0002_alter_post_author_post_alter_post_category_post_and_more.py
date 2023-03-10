# Generated by Django 4.1.5 on 2023-01-06 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categories.category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_post',
            field=models.TextField(verbose_name='Conteúdo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_post',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='post',
            name='exerpt_post',
            field=models.TextField(verbose_name='Excerto'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_post',
            field=models.ImageField(blank=True, null=True, upload_to='post_img/%Y/%m/%d', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pubished_post',
            field=models.BooleanField(default=False, verbose_name='Publicado'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_post',
            field=models.CharField(max_length=255, verbose_name='Título'),
        ),
    ]
