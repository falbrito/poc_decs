# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from Descritor.models import Descriptor, ScopeNote, Annotation
from Descritor.forms import DescriptorForm



# # usando TabularInline
# class PtInline(admin.TabularInline):
#     model = Pt

# usando StackedInline
class ScopeNoteInline(admin.StackedInline):
    model = ScopeNote
    classes = ['collapse']

class AnnotationInline(admin.StackedInline):
    model = Annotation
    classes = ['collapse']


class DescriptorForm(admin.ModelAdmin):
    # list_display = ('id_mesh','id_decs')
    list_display = ('descriptor_en','descriptor_es_la','descriptor_pt','descriptor_es_sp','descriptor_fr')

    # fields = ('id_mesh','id_decs')

    '''
    fieldsets = (
        (None, {
            'fields':('id_mesh','id_decs','descriptor_pt')
        }),
        ('Outros campos', {
            'classes': ('collapse',),
            'fields': ('descriptor_en','descriptor_es_la','descriptor_es_sp','descriptor_fr'),
        }),
    )
    '''

    form = DescriptorForm


    # Incluindo o formulario de Descriptor
    inlines = [
        ScopeNoteInline,
        AnnotationInline,
    ]

    search_fields = [ 'id_mesh','id_decs','descriptor_pt','descriptor_en','descriptor_es_la','descriptor_es_sp','descriptor_fr' ]


admin.site.register(Descriptor, DescriptorForm)
