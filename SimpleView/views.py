from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def index(request):
    return HttpResponse("Hello, SimpleView App!")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

#  异步视图函数
async def async_current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)