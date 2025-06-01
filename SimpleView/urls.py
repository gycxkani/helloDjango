from django.urls import path, include
from SimpleView import views

urlpatterns = [
    path("", views.index, name="index"),
    path("curdatetime/", views.current_datetime, name="current_datetime"),
    path("asynccurdatetime/", views.async_current_datetime, name="async_current_datetime"),
]