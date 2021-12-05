from django import template
from django.template import context
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse

from .models import Painting
from worker.tasks import populate_database


class IndexView(generic.ListView):
    template_name = 'api/artworks/index.html'
    context_object_name = 'artworks'

    def get_queryset(self):
        return Painting.objects.order_by('-created_at')[:5]


class DetailView(generic.DetailView):
    model = Painting
    template_name = 'api/artworks/detail.html'


def coucou(request):
    populate_database.s().delay()
    return HttpResponse('cc')
