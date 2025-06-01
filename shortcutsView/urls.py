from django.urls import path
from shortcutsView import views

urlpatterns = [
     path('renderdemo/', views.render_demo,  name='render_demo'),
     path('responsedemo/', views.http_response,  name='http_response'),
     path('redirectbaidu/', views.redirect_demo3,  name='redirect_demo3'),
]
