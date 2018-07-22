from django.http import HttpResponse
from django.shortcuts import render
from random import choice as rcho
import datetime as dt

def index(request):
    request.encoding = "UTF-8"
    randoms = [
        'dog', 'cat', 'teameow',
        'Hello World', 'meow',
        'Python', 'Django', 'runoob',
        'Google', 'Bing', 'DuckDuckGo',
        'Telegram', 'GitHub', 'TocasUI'
    ]
    vars = {}
    if "q" in request.GET:
        vars.update({'result': request.GET.get('q')})
    else:
        vars.update({'result': ""})
    timed = dt.datetime.now() + dt.timedelta(hours = 8)
    vars.update({'random': rcho(randoms)})
    vars.update({'time': timed})
    if "teameow" in request.GET:
        if request.GET['teameow'] == "pusheen":
            return HttpResponse("Pusheen 始春")
        else:
            return HttpResponse(r"<img src='https://yami.io/content/images/2016/10/photo_2016-10-18_04-15-06.jpg' alt='始春' /><p>始春</p>")
    else:
        return render(request, "index.html", vars)