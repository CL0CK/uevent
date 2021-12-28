from django.db import models
from django.urls import reverse

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Event text")
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", verbose_name="Photo")
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Time created")
    time_update = models.DateTimeField(
        auto_now=True, verbose_name="Time updated")
    is_published = models.BooleanField(
        default=True, verbose_name="Is published?")
    cat = models.ForeignKey(
        'Category', on_delete=models.PROTECT, verbose_name="Categories")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event', kwargs={'event_slug': self.slug})

    class Meta:
        verbose_name = "Ивент"
        verbose_name_plural = "Ивенты"
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(
        max_length=100, db_index=True, verbose_name="Category")
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']
