from django.shortcuts import render
from .models import *
from .forms import ContactForm


def start_page(request):
    context = {}
    pubs = Publication.objects.filter(type='publication')
    context.update({'pubs': pubs})
    return render(request, 'main_page.html', context)


def achievements_page(request):
    context = {}
    pubs = Publication.objects.filter(type='achievement')
    context.update({'pubs': pubs})
    return render(request, 'achievements_page.html', context)


def feedback_page(request):
    context = {}
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context.update({'thanks': True})
    return render(request, 'feedback_page.html', context)


def albums_page(request):
    context = {}
    context.update({'albums': Album.objects.all()})
    return render(request, 'albums_page.html', context)


def photos_page(request, albumid):
    context = {}
    context.update({'photos': Album.objects.get(id=albumid).photos.all()})
    return render(request, 'photos_page.html', context)
