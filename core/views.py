# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from core.models import Category, BasicItem, Content
import markdown

def get_markdown_item(item):
    item.description = markdown.markdown(item.description)
    return item

def index(request):
    basic = BasicItem.objects.first()
    basic.introduction = markdown.markdown(basic.introduction)

    categories_items = Category.objects.order_by('position').all()
    categories = []
    for category in categories_items:
        categories.append(get_markdown_item(category))

    return render(request, 'index.html', {'categories' : categories, 'basic' : basic})

def view_category(request, id):
    basic = BasicItem.objects.first()
    basic.introduction = markdown.markdown(basic.introduction)

    category = Category.objects.filter(id=id).order_by('position').first()
    category = get_markdown_item(category)

    content_items = Content.objects.filter(category=category).all()
    contents = []
    for content in content_items:
        contents.append(get_markdown_item(content))

    return render(request, 'content.html', {'category' : category, 'basic' : basic, 'contents' : contents})

