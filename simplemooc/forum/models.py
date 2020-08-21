from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

from django.db.models.signals import pre_save
from django.urls import reverse

#Tabela comentarios
class Thread(models.Model):
    title = models.CharField('Titulo', max_length=100)
    slug = models.SlugField('Identificador', unique=True)
    body = models.TextField('Mensagem')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Autor', related_name='threads',
        on_delete=models.SET_NULL, null=True
    )

    views = models.IntegerField('Visualizacoes', blank=True, default=0)
    answers = models.IntegerField('Respostas', blank=True, default=0)

    tags = TaggableManager()
    
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em ', auto_now=True)    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Forum:thread', kwargs={'slug': self.slug})


    class Meta:
        verbose_name='Topico'
        verbose_name_plural = 'Topicos'
        ordering = ['-modified']    

      


class Replay(models.Model):
    thread = models.ForeignKey(
        Thread, verbose_name='Topico', related_name='replies', 
        on_delete=models.SET_NULL, null=True
    )
    replay = models.TextField('Mensagem')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Replay', related_name='replies',
        on_delete=models.SET_NULL, null=True
    )
    correct = models.BooleanField('Correta?', blank=True, default=False)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em ', auto_now=True)

    def __str__(self):
        return self.replay[:50]


    class Meta:
        verbose_name='Resposta'
        verbose_name_plural='Respostas'
        ordering=['-correct','created']

