from django.db import models
from django.conf import settings
from django.utils import timezone
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
    
    


class Content(models.Model):
    title = models.CharField(max_length=100)
    cont = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null = True)
    tags = TaggableManager()
    image = models.ImageField(upload_to='images/', null =True)

    def publish(self):
        self.date_published = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

    def get_tags(self):
        tag_name = [tag.name for tag in self.tags.all()]
        return tag_name




