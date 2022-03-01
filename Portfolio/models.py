from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categoties')
    
    class Meta:
        ordering = ("name",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    
class Items(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='items')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ("name",)
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name