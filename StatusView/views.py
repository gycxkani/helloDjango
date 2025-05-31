from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. StatusView App!")
def status_code_view(request, scode):
    print("status code: ", scode)
    # 返回一个状态码
    return HttpResponse(status=scode)
