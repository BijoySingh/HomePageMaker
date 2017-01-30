from django.db import models


# Basic Information
class BasicItem(models.Model):
    ACCENT_COLORS = [("cyan","cyan"), ("light_blue","light_blue"), ("blue","blue"), ("indigo","indigo"),
                     ("deep_purple","deep_purple"), ("purple","purple"), ("pink","pink"), ("red","red"),
                     ("deep_orange","deep_orange"), ("orange","orange"), ("amber","amber"), ("yellow","yellow"),
                     ("lime","lime"), ("light_green","light_green"), ("green","green"), ("teal","teal")]
    PRIMARY_COLORS = ACCENT_COLORS + [("grey","grey"), ("blue_grey","blue_grey"), ("brown","brown")]

    name = models.CharField(max_length=256, default="")
    introduction = models.TextField(default="")
    profile = models.ImageField(null=True)
    cover = models.ImageField(null=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=256, default="")
    google = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    html_favicon = models.ImageField(null=True)
    html_keywords = models.TextField(default="", blank=True)
    html_description = models.TextField(default="", blank=True)
    html_title = models.TextField(default="", blank=True)
    discus_domain = models.CharField(default="", max_length=256, blank=True)
    primary_color = models.CharField(choices=PRIMARY_COLORS, max_length=20, default="red")
    accent_color = models.CharField(choices=ACCENT_COLORS, max_length=20, default="teal")
    theme_color = models.CharField(default="#dd1338", max_length=9)


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
    position = models.IntegerField(default=0)

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
