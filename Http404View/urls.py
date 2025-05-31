from django.urls import path, include
from Http404View import views


urlpatterns = [
    path('', views.index, name='index'),
    path('zeroexp/', views.zero_exp, name='zero_exp'),
]
