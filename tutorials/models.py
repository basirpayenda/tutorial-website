from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    cat_image = models.ImageField(upload_to='Category',null=True, blank=True)
    cat_title = models.CharField(max_length=250)
    cat_overview = models.CharField(max_length=500)
    cat_slug = models.SlugField(unique=True)

    def __str__(self):
        return self.cat_title

    def save(self, *args, **kwargs):
        self.cat_slug = slugify(self.cat_title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

class SubCategory(models.Model):
    sub_cat_image = models.ImageField(upload_to='SubCategory',null=True, blank=True)
    sub_cat_title = models.CharField(max_length=255)
    sub_cat_overview = models.CharField(max_length=500)
    sub_cat_parent = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_cat_slug = models.SlugField(unique=True)

    def __str__(self):
        return self.sub_cat_title

    def save(self, *args, **kwargs):
        self.sub_cat_slug = slugify(self.sub_cat_title)
        super(SubCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Sub categories'

class SubSubCategory(models.Model):
    subsub_cat_title = models.CharField(max_length=150)
    subsub_cat_parent = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
    subsub_cat_slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.subsub_cat_slug = slugify(self.subsub_cat_title)
        super(SubSubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.subsub_cat_title


class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=255)
    tutorial_parent = models.ForeignKey(SubSubCategory, on_delete = models.SET_NULL, null=True)
    tutorial_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tutorial_timestamp = models.DateTimeField(auto_now_add=True)
    tutorial_views = models.PositiveIntegerField(default=1)
    tutorial_content = models.TextField()
    tutorial_thumbnail = models.ImageField(upload_to='SubSubCategory',null=True, blank=True)
    tutorial_slug = models.SlugField(unique=True)

    def __str__(self):
        return self.tutorial_title

    def save(self, *args, **kwargs):
        self.tutorial_slug = slugify(self.tutorial_title)
        super(Tutorial, self).save(*args, **kwargs)


