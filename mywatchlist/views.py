from django.shortcuts import render
from mywatchlist.models import WatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_watchlist = WatchList.objects.all()
    total_watched = 0
    total_not_watched = 0
    has_watched_a_lot = False

    for data in data_watchlist:
        if data.watched:
            total_watched+=1
        else:
            total_not_watched+=1

    if total_watched >= total_not_watched:
        has_watched_a_lot = True
    
    context = {
        'list_watchlist': data_watchlist,
        'name': 'Maureen Esther Wijaya',
        'npm': '2106705335',
        'has_watched_a_lot': has_watched_a_lot
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_html(request):
    data_watchlist = WatchList.objects.all()
    context = {
        'list_watchlist': data_watchlist,
    }
    return render(request, "mywatchlist_data.html", context)