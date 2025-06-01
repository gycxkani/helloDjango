from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader


# Create your views here.


def render_demo(request):
    return render(
        request,
        'shortcutsView/index.html',
        {'foo': 'bar'},
        content_type='text/html',
    )


# 通过HttpResponse对象实现相同功能
def http_response(request):
    v_template = loader.get_template('shortcutsView/index.html')
    v_content = {'foo': 'bar'}
    return HttpResponse(
        v_template.render(v_content, request),
        content_type='text/html',
    )


def redirect_demo1(request, my_model=None):
    # 调用对象的get_absolute_url()方法
    obj = my_model.objects.get_absolute_url(...)
    return redirect(obj)


def redirect_demo2(request):
    # 通过视图名称和一些参数返回重定向URL
    return redirect('some-view-name', foo='bar')


def redirect_demo3(request):
    # 通过硬编码返回重定向URL
    return redirect('https://www.baidu.com')


def redirect_demo4(request):
    # 通过硬编码返回重定向URL
    return redirect('/page/content/detail/')



def redirect_demo5(request):
    # 返回一个永久重定向
    return redirect('/page/content/detail/', permanent=True)