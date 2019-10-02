from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=100)
    cont = models.TextField()
    datePublished = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def publish(self):
        self.datePublished = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title