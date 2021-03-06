# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


# Descriptor fields
class Descriptor(models.Model):

    # field tag 1
    descriptor_en = models.CharField( u'Inglês', max_length=200, null=True, blank=True )

    # field tag 2
    descriptor_es_la = models.CharField( u'Espanhol', max_length=200, null=True, blank=True )

    # field tag 3
    descriptor_pt = models.CharField( u'Português', max_length=200, null=True, blank=True )

    # field tag 4
    descriptor_es_sp = models.CharField( u'Espanhol - Espanha', max_length=200, null=True, blank=True )

    # filed tag 16
    descriptor_fr = models.CharField( u'Francês', max_length=200, null=True, blank=True )

    active_descriptor = models.BooleanField( u'Ativo', default=False, help_text=u'Marque para definir o Descritor como ativo.' )

    class Meta:
        verbose_name = u'Descritor'
        verbose_name_plural = u'Descritores'
        ordering = ['descriptor_pt']

    def __unicode__(self): # informação que retornará 
        # return '%s %s' % (self.id, self.descriptor_pt)
        # return self.id_mesh
        return '%s' % (self.descriptor_pt)


class UniqueIdentifier(models.Model):

    # field tag 99 or 999
    id_decs = models.CharField( u'Identificador DeCS', max_length=20, null=True, blank=True )

    # field tag 480
    id_mesh = models.CharField( u'Identificador MESH', max_length=20, null=True, blank=True )

    id_unique_identifier = models.OneToOneField(Descriptor)

    class Meta:
        verbose_name = u'Número Identificador'
        verbose_name_plural = u'Números Identificadores'

    def __unicode__(self): # informação que retornará 
        return '%s' % (self.id)



# Register type - v105 and v106
class RegisterType(models.Model):
    
    RECORD_TYPE_CHOICES = (
                            ('H','Heading'),('Q','Qualificador'),('T','Tipo de Publicação')
                        )
    # v105
    record_type = models.CharField( u'Tipo de Registro', 
                                    max_length=1, 
                                    choices=RECORD_TYPE_CHOICES, 
                                    null=True, 
                                    blank=True
                                )

    DESCRIPTOR_TYPE_CHOICES = (
                                ('m','MeSH'),
                                ('s','Saúde Pública'),
                                ('p','Homeopatia'),
                                ('f','Reforma Saúde'),
                                ('r','REPIDISCA'),
                                ('n','Não indexável'),
                                ('c','Pré-codificado'),
                                ('x','Exploded'),
                                ('g','Geográfico'),
                                ('z','Geo. DeCS'),
                                ('l','PT LILACS'),
                                ('d','Desastre'),
        )

    # v106
    descriptor_type = MultiSelectField( u'Tipo de Descritor',choices=DESCRIPTOR_TYPE_CHOICES, max_length=50, null=True, blank=True)

    id_register_type = models.OneToOneField(Descriptor)

    class Meta:
        verbose_name = u'Tipo'
        verbose_name_plural = u'Tipos'

    def __unicode__(self): # informação que retornará 
        return '%s' % (self.id)



# Tree numbers for descriptors
class TreeNumbersForDescriptors(models.Model):

    # v20
    tree_numbers = models.CharField( u'Categoria', max_length=200, null=True, blank=True )

    id_tree_numbers = models.ForeignKey(Descriptor)

    class Meta:
        verbose_name = u'Tree number for descriptor'
        verbose_name_plural = u'Tree numbers for descriptors'

    def __unicode__(self): # informação que retornará
        return '%s' % (self.id)


# Scope Note
class ScopeNote(models.Model):

    # field tag 5
    scope_note_en = models.TextField( u'Inglês', max_length=3000, null=True, blank=True )

    # field tag 6
    scope_note_es_la = models.TextField( u'Espanhol', max_length=3000, null=True, blank=True )

    # field tag 7
    scope_note_pt = models.TextField( u'Português', max_length=3000, null=True, blank=True )

    # field tag 8
    scope_note_es_sp = models.TextField( u'Espanhol - Espanha', max_length=3000, null=True, blank=True )

    # field tag not exist before
    scope_note_fr = models.TextField( u'Francês', max_length=3000, null=True, blank=True )

    id_scope_note = models.OneToOneField(Descriptor)

    class Meta:
        verbose_name = u'Definição'
        verbose_name_plural = u'Definições'

    def __unicode__(self): # informação que retornará
        return '%s' % (self.id)


# Annotation
class Annotation(models.Model):

    # field tag 110
    annotation_en = models.TextField( u'Inglês', max_length=1500, null=True, blank=True )

    # field tag 210
    annotation_es_la = models.TextField( u'Espanhol', max_length=1500, null=True, blank=True )

    # field tag 310
    annotation_pt = models.TextField( u'Português', max_length=1500, null=True, blank=True )

    # field tag not exist before
    annotation_es_sp = models.TextField( u'Espanhol - Espanha', max_length=1500, null=True, blank=True )

    # field tag not exist before
    annotation_fr = models.TextField( u'Francês', max_length=1500, null=True, blank=True )

    id_annotation = models.OneToOneField(Descriptor)

    class Meta:
        verbose_name = u'Nota de Indexação'
        verbose_name_plural = u'Notas de Indexação'

    def __unicode__(self): # informação que retornará
        return '%s' % (self.id)


# Synonym
class Synonym(models.Model):

    # v50^i
    synonym_en = models.CharField( u'Inglês', max_length=200, null=True, blank=True )

    # v50^e
    synonym_es_la = models.CharField( u'Espanhol', max_length=200, null=True, blank=True )

    # v50^p
    synonym_pt = models.CharField( u'Português', max_length=200, null=True, blank=True )

    # v50^s
    synonym_es_sp = models.CharField( u'Espanhol - Espanha', max_length=200, null=True, blank=True )

    # field tag not exist before
    synonym_fr = models.CharField( u'Francês', max_length=200, null=True, blank=True )

    id_synonym = models.ForeignKey(Descriptor)

    class Meta:
        verbose_name = u'Sinônimo'
        verbose_name_plural = u'Sinônimos'

    def __unicode__(self): # informação que retornará
        return '%s' % (self.id)


# Non-Print Entry Term
class NonPrintEntryTerm(models.Model):

    # v23^i
    npe_en = models.CharField( u'Inglês', max_length=200, null=True, blank=True )

    id_npe = models.ForeignKey(Descriptor)

    class Meta:
        verbose_name = u'Non-Print Entry Term'
        verbose_name_plural = u'Non-Print Entry Terms'

    def __unicode__(self): # informação que retornará
        return '%s' % (self.id)



class OnlineNote(models.Model):

    # v117 - en
    online_note_en = models.TextField( u'Inglês', max_length=1500, null=True, blank=True )

    # v217 - es
    online_note_es_la = models.TextField( u'Espanhol', max_length=1500, null=True, blank=True )

    # v317 - pt
    online_note_pt = models.TextField( u'Português', max_length=1500, null=True, blank=True )

    id_online_note = models.OneToOneField(Descriptor)

    class Meta:
        verbose_name = u'Nota Online'
        verbose_name_plural = u'Notas Online'

    def __unicode__(self): # informação que retornará
        return '%s' % (self.id)



class HistoryNote(models.Model):

    # v119 - en
    history_note_en = models.TextField( u'Inglês', max_length=1500, null=True, blank=True )

    # v219 - es
    history_note_es_la = models.TextField( u'Espanhol', max_length=1500, null=True, blank=True )

    # v319 - pt
    history_note_pt = models.TextField( u'Português', max_length=1500, null=True, blank=True )

    id_history_note = models.OneToOneField(Descriptor)

    class Meta:
        verbose_name = u'Nota Histórica'
        verbose_name_plural = u'Notas Históricas'

    def __unicode__(self): # informação que retornará
        return '%s' % (self.id)

class AllowedQualifiers(models.Model):

    # v950
    allowed_qualifier = models.TextField( u'Qualificador permitido', max_length=200, null=True, blank=True )

    id_allowed_qualifier = models.OneToOneField(Descriptor)

    class Meta:
        verbose_name = u'Qualificador Permitido'
        verbose_name_plural = u'Qaulificadores Permitidos'

    def __unicode__(self): # informação que retornará
        return '%s' % (self.id)    