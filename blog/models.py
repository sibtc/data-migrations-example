from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title
