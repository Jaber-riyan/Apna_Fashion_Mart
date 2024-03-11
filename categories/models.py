from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=100, null=True, blank=True, unique=True)
    
    def __str__(self):
        return self.category_name