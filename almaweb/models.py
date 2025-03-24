from django.db import models
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    document = models.FileField(upload_to='documents/')
    author = models.CharField(max_length=100) 
    published_date = models.DateField(default=timezone.now) 
    def __str__(self):
        return self.title