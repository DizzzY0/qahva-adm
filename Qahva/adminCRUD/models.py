from django.db import models

class Category(models.Model):
   
    # category_id = models.CharField(max_length=50, unique=True)
    name_ru = models.CharField(max_length=255)
    name_uz = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description_ru = models.TextField()
    description_uz = models.TextField()
    category_icon = models.FileField(upload_to='category_icons/', null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_ru
