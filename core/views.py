# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from core.models import Category, BasicItem


def index(request):
    basic = BasicItem.objects.first()
    categories = Category.objects.order_by('position').all()
    return render(request, 'index.html', {'categories' : categories, 'basic' : basic})
