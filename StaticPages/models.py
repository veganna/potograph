from django.db import models

# Create your models here.

class HeroCarrousel(models.Model):
    image = models.ImageField(upload_to='hero_carrousel')
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    class meta:
        verbose_name = "Hero Carrousel"
        verbose_name_plural = "Hero Carrousel Items"

class experience(models.Model):
    image = models.ImageField(upload_to='experience')
    title = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.title
    class meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"