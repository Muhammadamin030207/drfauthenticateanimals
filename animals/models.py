from django.db import models
from django.utils.text import slugify


class Animal(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    scientific_name = models.CharField(max_length=150)
    species = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    habitat = models.TextField()
    diet = models.CharField(max_length=100)
    lifespan = models.PositiveSmallIntegerField(help_text="Average lifespan in years")
    weight = models.DecimalField(max_digits=8, decimal_places=2, help_text="Average weight in kg")
    height = models.DecimalField(max_digits=6, decimal_places=2, help_text="Average height in cm")
    conservation_status = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='animals/images/', blank=True, null=True)
    is_endangered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'animals_animal'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name