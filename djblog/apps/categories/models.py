from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    # slug = models.SlugField(max_length=255, unique=True, blank=True)
    slug = models.CharField(max_length=255,  blank=True)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title




