from django import forms
from .models import Upload

class imageUploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('quality','image',)