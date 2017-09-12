# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

''' v1, v2, v3, v4, v16 '''
class Descriptor(models.Model):

    descriptor_en = models.CharField( u'Inglês', max_length=200, null=True, blank=True )
    descriptor_es_la = models.CharField( u'Espanhol', max_length=200, null=True, blank=True )
    descriptor_pt = models.CharField( u'Português', max_length=200, null=True, blank=True )
    descriptor_es_sp = models.CharField( u'Espanhol - Espanha', max_length=200, null=True, blank=True )
    descriptor_fr = models.CharField( u'Francês', max_length=200, null=True, blank=True )
    active_descriptor = models.BooleanField( u'Ativo', default=True, help_text=u'Marque para definir o Descritor como ativo.' )

    class Meta:
        verbose_name = u'Descritor'
        verbose_name_plural = u'Descritores'
        ordering = ['descriptor_pt']


    def __unicode__(self): # informação que retornará 
        # return '%s %s' % (self.id, self.descriptor_pt)
        # return self.id_mesh
        return '%s' % (self.descriptor_pt)


''' v5, v6, v7, v8 '''
class ScopeNote(models.Model):

    scope_note_en = models.TextField( u'Inglês', max_length=200, null=True, blank=True )
    scope_note_es_la = models.TextField( u'Espanhol', max_length=200, null=True, blank=True )
    scope_note_pt = models.TextField( u'Português', max_length=200, null=True, blank=True )
    scope_note_es_sp = models.TextField( u'Espanhol', max_length=200, null=True, blank=True )
    scope_note_fr = models.TextField( u'Francês', max_length=200, null=True, blank=True )
    id_scope_note = models.OneToOneField(Descriptor)

    class Meta:
        verbose_name = u'Definição'
        verbose_name_plural = u'Definições'

    def __unicode__(self): # informação que retornará
        return '%s' % (self.id)


''' v110, v210 v310 '''
class Annotation(models.Model):

    annotation_en = models.TextField( u'Inglês', max_length=200, null=True, blank=True )
    annotation_es_la = models.TextField( u'Espanhol', max_length=200, null=True, blank=True )
    annotation_pt = models.TextField( u'Portugês', max_length=200, null=True, blank=True )
    annotation_es_sp = models.TextField( u'Espanhol - Espanha', max_length=200, null=True, blank=True )
    annotation_fr = models.TextField( u'Francês', max_length=200, null=True, blank=True )
    id_annotation = models.OneToOneField(Descriptor)

    class Meta:
        verbose_name = u'Nota de Indexação'
        verbose_name_plural = u'Notas de Indexação'

    def __unicode__(self): # informação que retornará
        return '%s' % (self.id)





