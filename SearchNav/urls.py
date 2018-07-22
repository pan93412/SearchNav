from django.conf.urls import url
from . import view

# urlpatterns URL 模式
urlpatterns = [
    url(r'^$', view.index),
]