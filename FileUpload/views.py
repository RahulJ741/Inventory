# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import FileUploadForm

# Create your views here.


def checkfile(request):
    form = FileUploadForm(widget=forms.FileInput(attrs={'accept':['application/pdf']}))
    return render(request,'file_upload.html', {'form':form})
    



# NOTE: this code is used in models validations
# def validate_file_extension(value):
#     import os
#     from django.core.exceptions import ValidationError
#     ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
#     valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
#     if not ext.lower() in valid_extensions:
#         raise ValidationError(u'Unsupported file extension.')
