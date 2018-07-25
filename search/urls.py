from django.urls import path
from . import view

urlpatterns = [
    path('', view.search),
    path('teameow/', view.teameow),
    path('<search_query>/', view.autor)
]