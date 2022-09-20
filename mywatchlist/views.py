from django.shortcuts import render
from mywatchlist.models import WatchList

# Create your views here.
def show_mywatchlist(request):
    data_watchlist = WatchList.objects.all()
    context = {
        'list_watchlist': data_watchlist,
        'name': 'Maureen Esther Wijaya',
        'npm': '2106705335'
    }
    return render(request, "mywatchlist.html", context)
