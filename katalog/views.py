from multiprocessing import context
from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
        'item_list' : data_katalog,
        'name' : 'Maureen Esther Wijaya',
        'npm' : '2106705335'
    }
    return render(request, "katalog.html", context)
