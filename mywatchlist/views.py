from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data = MyWatchList.objects.all()
    already_watch = 0
    not_watch = 0

    for title in data:
        if title.watched == True:
            already_watch += 1
        else:
            not_watch +=1 
        
    if already_watch >= not_watch:
        msg = "Selamat, kamu sudah banyak menonton!"
    else:
        msg = "Wah, kamu masih sedikit menonton!"

    context = {
        'list_item': data,
        'nama': 'Daffa Maulana Haekal',
        'id': '2106652083',
        'message': msg
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def show_html(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("html", data), content_type="application/html")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        
def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_html_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    already_watch = 0
    not_watch = 0

    for title in data:
        if title.watched == True:
            already_watch += 1
        else:
            not_watch +=1 
        
    if already_watch >= not_watch:
        msg = "Selamat, kamu sudah banyak menonton!"
    else:
        msg = "Wah, kamu masih sedikit menonton!"

    context = {
        'list_item': data,
        'nama': 'Daffa Maulana Haekal',
        'id': '2106652083',
        'message': msg
    }
    return render(request, "mywatchlist.html", context)