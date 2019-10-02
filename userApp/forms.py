from django import forms
from .models import Content

class contentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title','cont']
