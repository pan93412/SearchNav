# 匯入相關模組
from django.http import HttpResponse
from django.template import loader
import os, random, json, time, datetime

# 隨機字母產生器
random_str = ""
strtmp = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg\
hijklmnopqrstuvwxyz0123456789"
for _ in range(0, 7):
    random_str += random.choice(strtmp)
del strtmp


# 定義變數
random_list = [
    'Google', 'Bing', 'DuckDuckGo', 'TeaMeow', "Meow", "Tocas+UI", "始春",
    "runoob", "Yami Odymel", "Yahoo",
]
search_var = {'random_code': random_str}
startTime = time.time()

# '/teameow' 始春區塊
def teameow(r):
    return HttpResponse(r"<img src='https://yami.io/content/images/2016/10/photo_2016-10-18_04-15-06.jpg'\
alt='始春' title='何時始春會到來？我看永遠不會來！' width='400' height='400' /><p>始春</p>")

# '/' 搜尋區塊
def search(r):
    r.encoding = "UTF-8" # 設定編碼
    search_var.update({'random': random.choice(random_list)}) # 「試試手氣？」功能

    # 伺服器啟動時間與目前時間部份
    search_var.update({
        'start_time': time.asctime(time.localtime(startTime)),
        'now_time': datetime.datetime.now() + datetime.timedelta(hours = 8),
    })

    # 接收使用者的搜尋請求，並給出回應。
    if r.GET.get("q", "") == "":
        search_var.update({'result': ""})
    else:
        search_var.update({'result': r.GET.get("q")})
    
   # 渲染 search.html 並呈現給客戶端
    return HttpResponse(loader.get_template("search.html").render(search_var))

# 若使用者輸入錯誤之後的導向
def autor(r, search_query):
    tp = loader.get_template("not_found.html")
    var = {
        'search': search_query,
        'start_time': time.asctime(time.localtime(startTime)),
        'now_time': datetime.datetime.now() + datetime.timedelta(hours = 8),
        'random_code': random_str
    }
    return HttpResponse(tp.render(var, r))