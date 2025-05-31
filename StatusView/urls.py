from django.urls import path, include
from StatusView import views


urlpatterns = [
    path('', views.index, name='index'),
    path('statuscode/<int:scode>/', views.status_code_view, name='status_code_view'),
]
