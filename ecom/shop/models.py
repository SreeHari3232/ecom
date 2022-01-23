from django.db import models
from django.db.models.base import Model
from django.db.models.fields.files import ImageField

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=45)
    # image = models.ImageField(upload_to='category')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    image = models.ImageField(upload_to='product')
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text =models.TextField(max_length=200, verbose_name='Preview Text')
    description = models.TextField(max_length=1000, verbose_name='Description')
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['created',]
    
        