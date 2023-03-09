from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='likes')

    def get_absolute_url(self):
        return '/'
