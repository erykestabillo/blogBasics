from django.forms import ModelForm
from .models import Content, Category

class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['title','cont','category','tags','image']
    





