from django.urls import path, include
from ErrorView import views


urlpatterns = [
    path('', views.index, name='index'),
    path('pagenotfound/<int:p>/', views.error_view, name='error_view'),
]