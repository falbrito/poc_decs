# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Descriptor(models.Model):

    class Meta:
        verbose_name = u'Descritor'
        verbose_name_plural = u'Descritores'

    ''' v1, v2, v3, v4, v16 '''
    id_mesh = models.CharField( u'ID MESH', max_length=50, null=True, blank=True )
    id_decs = models.CharField( u'ID DeCS', max_length=50, null=True, blank=True )
    descriptor_en = models.CharField( u'Inglês', max_length=200, null=True, blank=True )
    descriptor_es_la = models.CharField( u'Espanhol', max_length=200, null=True, blank=True )
    descriptor_pt = models.CharField( u'Português', max_length=200, null=True, blank=True )
    descriptor_es_sp = models.CharField( u'Espanhol - Espanha', max_length=200, null=True, blank=True )
    descriptor_fr = models.CharField( u'Francês', max_length=200, null=True, blank=True )

    def __unicode__(self): # informação que retornará 
        # return '%s %s' % (self.id, self.descriptor_pt)
        # return self.id_mesh
        return '%s' % (self.descriptor_pt)


class ScopeNote(models.Model):

    class Meta:
        verbose_name = u'Definição'
        verbose_name_plural = u'Definições'

    ''' v5, v6, v7, v8 '''
    scope_note_en = models.TextField( u'Inglês', max_length=200, null=True, blank=True )
    scope_note_es_la = models.TextField( u'Espanhol', max_length=200, null=True, blank=True )
    scope_note_pt = models.TextField( u'Português', max_length=200, null=True, blank=True )
    scope_note_es_sp = models.TextField( u'Espanhol', max_length=200, null=True, blank=True )
    scope_note_fr = models.TextField( u'Francês', max_length=200, null=True, blank=True )
    id_scope_note = models.OneToOneField(Descriptor)

    def __unicode__(self): # informação que retornará
        return self.scope_note_pt


class Annotation(models.Model):

    class Meta:
        verbose_name = u'Nota de Indexação'
        verbose_name_plural = u'Notas de Indexação'

    ''' v110, v210 v310 '''
    annotation_en = models.TextField( u'Inglês', max_length=200, null=True, blank=True )
    annotation_es_la = models.TextField( u'Espanhol', max_length=200, null=True, blank=True )
    annotation_pt = models.TextField( u'Portugês', max_length=200, null=True, blank=True )
    annotation_es_sp = models.TextField( u'Espanhol - Espanha', max_length=200, null=True, blank=True )
    annotation_fr = models.TextField( u'Francês', max_length=200, null=True, blank=True )
    id_annotation = models.OneToOneField(Descriptor)

    def __unicode__(self): # informação que retornará
        return self.id_annotation





