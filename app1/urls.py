from django.urls import path, re_path, include, register_converter
from . import views, urlconverter

register_converter(urlconverter.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('articles/2023/', views.special_case_2023),
    path('articles/<yyyy:year>/', views.year_archive),
    path('articles/<yyyy:year>/<int:month>/', views.month_archive),
    path('articles/<yyyy:year>/<int:month>/<int:day>/', views.day_archive),
    path('articles/<yyyy:year>/<int:month>/<int:day>/<slug:slug>/', views.article_detail),
]
