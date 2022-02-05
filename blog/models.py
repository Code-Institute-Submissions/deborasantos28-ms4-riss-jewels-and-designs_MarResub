from django.db import models

# Create your models here.
from django.core.validators import MaxLengthValidator

from django.contrib.auth.models import User


class BlogEntry(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_entry')
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    image = models.ImageField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):

    post = models.ForeignKey(BlogEntry, on_delete=models.CASCADE,
                             related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(validators=[MaxLengthValidator(500)])
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return '{} by {}'.format(self.body, self.username)