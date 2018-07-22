from django.conf.urls import url
from django.contrib import admin
from . import view

# urlpatterns URL 模式
urlpatterns = [
    url(r'^$', view.index),
    url(r'^control/', admin.site.urls)
]