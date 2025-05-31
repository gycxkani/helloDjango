from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

def index(request):
    return HttpResponse("Hello, Http404View App!")
def zero_exp(request):
    try:
        r = 1 / 0
    except :
        raise Http404("1 / 0 does not exist")  # 抛出Http404错误
    return render(request, 'template/arithm.html', {'r': r})