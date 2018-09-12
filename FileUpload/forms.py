from django import forms



class FileUploadForm(forms.Form):
    file_uploaded = forms.FileField()
    
