from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_wishlist(request):
    data_item = CatalogItem.objects.all()
    context = {
        'list_item': data_item,
        'nama': 'Daffa Maulana Haekal',
        'id': '2106652083'
    }
    return render(request, "katalog.html", context)