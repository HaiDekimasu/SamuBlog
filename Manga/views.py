from django.http import HttpResponse
from django.shortcuts import render
from .models import Manga
from urllib.request import urlopen
# Create your views here.
def manga(request):
    mangas = Manga.objects.all()
    return render(request, 'manga.html', {'mangas': mangas})



def Tomo1(request):
    pdf_url = "https://ia803407.us.archive.org/33/items/kbbklv20210505manga1994runounikenshinnobuhirowatsuki/Manga/%281994%29%20Runouni%20Kenshin%20%28Nobuhiro%20Watsuki%29/Rurouni%20Kenshin%20-%20Tomo%2001%20%28%23001-008%29.pdf"
    pdf_file = urlopen(pdf_url)
    response = HttpResponse(pdf_file.read(), content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="Rurouni Kenshin - Tomo 01.pdf"'
    return response

def Tomo2(request):
    pdf_url = "https://ia803407.us.archive.org/33/items/kbbklv20210505manga1994runounikenshinnobuhirowatsuki/Manga/%281994%29%20Runouni%20Kenshin%20%28Nobuhiro%20Watsuki%29/Rurouni%20Kenshin%20-%20Tomo%2002%20%28%23009-020%29.pdf"
    pdf_file = urlopen(pdf_url)
    response = HttpResponse(pdf_file.read(), content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="Rurouni Kenshin - Tomo 02.pdf"'
    return response

def Tomo3(request):
    pdf_url = "https://ia803407.us.archive.org/33/items/kbbklv20210505manga1994runounikenshinnobuhirowatsuki/Manga/%281994%29%20Runouni%20Kenshin%20%28Nobuhiro%20Watsuki%29/Rurouni%20Kenshin%20-%20Tomo%2003%20%28%23021-028%29.pdf"
    pdf_file = urlopen(pdf_url)
    response = HttpResponse(pdf_file.read(), content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="Rurouni Kenshin - Tomo 03.pdf"'
    return response