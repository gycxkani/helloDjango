from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import requires_csrf_token

# Create your views here.
def index(request):
    return HttpResponse("Hello, ErrorView App!")

def error_view(request, p):
    print('p= ', p)
    if p:
        return HttpResponse("Page not found!")
    else:
        return HttpResponseNotFound("HttpResponseNotFound---Page not found!")

@requires_csrf_token
def bad_request(request, exception):
    return render(request, 'error/400.html')

@requires_csrf_token
def permission_denied(request, exception):
    return render(request, 'error/403.html')

@requires_csrf_token
def page_not_found(request, exception):
    return render(request, 'error/404.html')

@requires_csrf_token
def error(request):
    return render(request, 'error/500.html')