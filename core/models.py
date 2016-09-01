from django.db import models


# Basic Information
class BasicItem(models.Model):
    name = models.CharField(max_length=256, default="")
    introduction = models.TextField(default="")
    profile = models.ImageField(null=True, blank=True)
    cover = models.ImageField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=256, default="")
    google = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    html_favicon = models.ImageField(null=True, blank=True)
    html_keywords = models.TextField(default="")
    html_description = models.TextField(default="")
    html_title = models.TextField(default="")


# Category
class Category(models.Model):
    title = models.CharField(max_length=256, default="")
    description = models.TextField(default="")
    modified_at = models.DateTimeField(auto_now=True, auto_created=True)
    image = models.ImageField(blank=True, null=True)
    position = models.IntegerField(unique=True, default=0)
    span = models.IntegerField(default=3)
    direct_link = models.CharField(default="", null=True, blank=True, max_length=256)

    def __str__(self):
        return "[" + str(self.id) + "] " + self.title


# Content
class Content(models.Model):
    category = models.ForeignKey(Category, related_name='content')
    title = models.CharField(max_length=256, default="")
    description = models.TextField(default="")
    modified_at = models.DateTimeField(auto_now=True, auto_created=True)
    cover = models.ImageField(blank=True, null=True)
    gallery_object = models.BooleanField(default=False)

    def __str__(self):
        return "[" + str(self.category.id) + "][" + str(self.id) + "] " + self.title


# Content Image
class ContentImage(models.Model):
    content = models.ForeignKey(Content, related_name='image')
    caption = models.CharField(max_length=256, default="")
    modified_at = models.DateTimeField(auto_now=True, auto_created=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return "[" + str(self.content.id) + "][" + str(self.id) + "] " + self.caption
