from django.db import models
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.utils.text import slugify
import json

class ArticleQuerySet(models.QuerySet):
    def serialize(self):
        list_value = list(self.values("id", "title", "subtitle", "slug", "author", "post", "image_url", "status"))
        return json.dumps(list_value)

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model,using=self._db)

options = (
('draft', 'Draft'),
('published', 'Published'),
)


class Article(models.Model):
    title = models.CharField(max_length=127,unique=True, verbose_name="Title")
    subtitle = models.CharField(max_length=255, verbose_name="Description")
    image_url = models.URLField(max_length=255, verbose_name="Image URL")
    post = models.TextField(verbose_name='Content')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=16, choices=options, default='Draft')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=127)

    objects = ArticleManager() 

    def __str__(self):
        return self.title

    def serialize(self):
        data = {
            "id": self.id,
            "title": self.title,
            "subtitle": self.subtitle,
            "author": self.author.id,
            "image_url": self.image_url,
            "slug": self.slug,
            "status": self.status,
            "post": self.post,
        }
        data = json.dumps(data)
        return data
    
    def save(self, *args, **kwargs):
        self.slug = self.generate_slug()
        return super().save(*args, **kwargs)

    def generate_slug(self):
        generate_slug = slugify(self.title)
        return generate_slug

    class Meta:
        verbose_name_plural = 'Articles'
