from django import forms
from .models import Plant

class ImageUploadForm(forms.Form):   
   model = Plant
   fields = ['plantName', 'plantAlt', 'level', 'evn', 'desc', 'poster', 'plantImg']

# class ImageUploadForm(forms.ModelForm):

#    class Meta:
#       model = Plant
#       fields = ['plantName', 'plantAlt', 'level', 'evn', 'desc', 'poster', 'plantImg']