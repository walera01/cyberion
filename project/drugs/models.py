from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Drugs(models.Model):
    name = models.CharField(max_length=240, verbose_name="название")
    description = models.TextField()
    img = models.ImageField(verbose_name="Изображение")
    prise = models.FloatField()
    subcategory=models.ForeignKey('SubCategory', on_delete=models.PROTECT, blank=True, null=True, verbose_name="подкатегории")
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('drugs', kwargs={'drug':self.pk})

class Category(models.Model):
    name=models.CharField(max_length=50, db_index=True, verbose_name='Категория')
    icon = models.ImageField(blank=True)
    slug = models.SlugField(unique=True, db_index = True, verbose_name="URL")


    def  __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug':self.slug})


class SubCategory(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Категория')
    icon = models.ImageField(blank=True)
    slug = models.SlugField(unique=True, db_index=True, verbose_name="URL")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subcategory', kwargs={'subcategory_slug': self.slug})

# class Basket(AbstractUser):
#     drug = models.ManyToManyField(Drugs, verbose_name="Товар в карзине")
#     buyer = models.ManyToManyField(AbstractUser,  verbose_name="покупатель_корзины")


class Message(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    text = models.CharField(max_length=255)