"""
URL configuration for helloDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.static import serve
# from django.utils.translation import gettext_lazy as _
from ErrorView import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('app1/', include('app1.urls')),
    path('simple/', include('SimpleView.urls')),
    path('error/', include('ErrorView.urls')),
    path('status/', include('StatusView.urls')),
    path('http404/', include('Http404View.urls')),
    path('shortcutsView/', include('shortcutsView.urls')),

]   # + staticfiles_urlpatterns()+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = views.bad_request
handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.error

# if settings.DEBUG:
#     urlpatterns += [static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
#                     static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)]
# else:
#     urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
#                     re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]


if settings.DEBUG:
    urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
                    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})]


# 添加i18n URL配置
# urlpatterns += [
#     path(_('^i18n/'), include('django.conf.urls.i18n')),
# ]
