from .models import video_site, video_canal
from django.shortcuts import render
import random

def siteprincipal(request, id):

    site = video_site.objects.get(codigo=id)
    videos = video_canal.objects.all()

    selecionado = random.choice(videos)

    return render(request, 'red/siteprincipal.html', {'site':site, 'canal':selecionado})
