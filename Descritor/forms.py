# -*- coding: utf-8 -*-

from django import forms

from Descritor.models import Descriptor

class DescriptorForm(forms.ModelForm):

    class Meta:
        model = Descriptor
        # fields = '__all__'
        exclude = ()

