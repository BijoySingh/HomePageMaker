from django.contrib import admin

# Register your models here.
from core.models import Content, BasicItem
from core.models import ContentImage, Category

admin.site.register(BasicItem)
admin.site.register(Category)
admin.site.register(Content)
admin.site.register(ContentImage)
