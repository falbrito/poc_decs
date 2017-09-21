# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from Descritor.models import *

'''
Descriptor, 
TreeNumbersForDescriptors, 
NonPrintEntryTermScopeNote, 
Annotation, 
Synonym, 
RegisterType, 
OnlineNote, 
HistoryNote
'''

from Descritor.forms import DescriptorForm



# # usando TabularInline
# class PtInline(admin.TabularInline):
#     model = Pt

class RegisterTypeInline(admin.StackedInline):

    model = RegisterType
    classes = ['collapse']


class TreeNumbersForDescriptorsInline(admin.StackedInline):

    model = TreeNumbersForDescriptors
    extra = 1
    classes = ['collapse']

class NonPrintEntryTermInline(admin.StackedInline):

    model = NonPrintEntryTerm
    extra = 1
    classes = ['collapse']

# usando StackedInline
class ScopeNoteInline(admin.StackedInline):

    model = ScopeNote
    extra = 0
    classes = ['collapse']


class AnnotationInline(admin.StackedInline):

    model = Annotation
    extra = 0
    classes = ['collapse']


class SynonymInline(admin.StackedInline):

    model = Synonym
    extra = 1
    classes = ['collapse']


class OnlineNoteInline(admin.StackedInline):

    model = OnlineNote
    extra = 0
    classes = ['collapse']


class HistoryNoteInline(admin.StackedInline):

    model = HistoryNote
    extra = 0
    classes = ['collapse']


class DescriptorForm(admin.ModelAdmin):

    list_display = (
                    'active_descriptor',
                    'descriptor_en',
                    'descriptor_es_la',
                    'descriptor_pt',
                    'descriptor_es_sp',
                    'descriptor_fr'
                    )

    form = DescriptorForm


    # Incluindo o formulario de Descriptor
    inlines = [

        RegisterTypeInline,
        TreeNumbersForDescriptorsInline,
        ScopeNoteInline,
        AnnotationInline,
        SynonymInline,
        NonPrintEntryTermInline,
        OnlineNoteInline,
        HistoryNoteInline,   
    
    ]

    search_fields = [ 
                    'id_mesh',
                    'id_decs',
                    'descriptor_pt',
                    'descriptor_en',
                    'descriptor_es_la',
                    'descriptor_es_sp',
                    'descriptor_fr'
                    ]


admin.site.register(Descriptor, DescriptorForm)
