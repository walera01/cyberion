from django.db import models
from django.urls import reverse


class Drugs(models.Model):
    name = models.CharField(max_length=240)
    description = models.TextField()
    img = models.ImageField()
    prise = models.FloatField()
    category=models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории")
    
    def  __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('drugs', kwargs={'drug':self.pk})

class Category(models.Model):
    name=models.CharField(max_length=50, db_index=True, verbose_name='Категория')
    slug = models.SlugField(unique=True, db_index = True, verbose_name="URL")

    def  __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug':self.slug})



class Message(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    text = models.CharField(max_length=255)