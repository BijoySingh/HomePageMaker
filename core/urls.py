from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)/$', views.view_category, name='view_category'),
]