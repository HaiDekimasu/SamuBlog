from django.shortcuts import render
from .models import Capitulos
from django.contrib.auth.decorators import permission_required
from django.http import  HttpResponseRedirect

@permission_required("capitulos.can_create_capitulos")
def capitulos(request):
    if request.method == "POST":
        title = request.POST["title"]
        text = request.POST["text"]
        iframe_url = request.POST["iframe_url"]
        capitulos = Capitulos.objects.create(
            title=title,
            text=text,
            iframe_url=iframe_url,
        )

        return HttpResponseRedirect("/")

    capitulos = Capitulos.objects.all()
    return render(request, 'capitulos.html',{'capitulos': capitulos})
