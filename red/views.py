from .models import video_site, video_canal
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def siteprincipal(request, id):
    return render(request, 'red/siteprincipal.html')
