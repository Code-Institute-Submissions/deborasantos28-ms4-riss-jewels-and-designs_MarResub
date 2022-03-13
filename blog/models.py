from django.db import models
from django.core.validators import MaxLengthValidator

from django.contrib.auth.models import User


class BlogPost(models.Model):
    '''A model for the Blog main information
    and parameters. In this model resides all of
    the key fields for the Blog'''

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        related_name="blog_posts"
    )
    title = models.CharField(
        max_length=100, unique=True)
    slug = models.SlugField(
        max_length=100, unique=True)
    content = models.TextField()
    image = models.ImageField()
    date_posted = models.DateTimeField(
        auto_now_add=True)

    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    '''A model for the Comment section's
    parameters. In this model resides all of
    the key fields and body format of the
    Comment section'''

    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE,
        related_name="comments"
    )
    username = models.ForeignKey(
        User, on_delete=models.CASCADE)
    body = models.TextField(
        validators=[MaxLengthValidator(500)])
    date_posted = models.DateTimeField(
        auto_now_add=True)

    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return "{} by {}".format(
            self.body, self.username)
