from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def special_case_2023(request):
    return HttpResponse('This page is for year 2023.')

def  year_archive(request, year):
    return HttpResponse(f'This page is for year {year}.')

def month_archive(request, year, month):
    return HttpResponse(f'This page is for year {year}, month {month}.')

def day_archive(request, year, month, day):
    return HttpResponse(f'This page is for year {year}, month {month}, day {day}.')

def article_detail(request, year, month, day, slug):
    return HttpResponse(f'This page is for year {year}, month {month}, day {day}, slug {slug}.')