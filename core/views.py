# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from core.models import Category, BasicItem, Content


def index(request):
    basic = BasicItem.objects.first()
    categories = Category.objects.order_by('position').all()
    return render(request, 'index.html', {'categories' : categories, 'basic' : basic})


def view_category(request, id):
    basic = BasicItem.objects.first()
    category = Category.objects.filter(id=id).first()
    contents = Content.objects.filter(category=category).all()
    return render(request, 'content.html', {'category' : category, 'basic' : basic, 'contents' : contents})

