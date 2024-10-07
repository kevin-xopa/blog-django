from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    published = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.title