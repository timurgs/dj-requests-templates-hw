from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


with open(settings.BUS_STATION_CSV, encoding='utf-8') as file:
    reader = csv.DictReader(file)
    STATION_LIST = [row for row in reader]


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    elements_per_page = 10
    paginator = Paginator(STATION_LIST, elements_per_page)
    page = paginator.get_page(page_number)
    content = page.object_list

    context = {
        'bus_stations': content,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
