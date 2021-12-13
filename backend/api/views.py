from django import template
from django.template import context
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Painting
from worker.tasks import populate_database


class IndexView(generic.ListView):
    template_name = 'paintings/index.html'
    context_object_name = 'paintings'

    def get_queryset(self):
        paintings_query = Painting.repository.with_picture().with_readable_name()

        return paintings_query.order_by('-created_at')[:50]


class DetailView(generic.DetailView):
    model = Painting
    template_name = 'paintings/detail.html'


def coucou(request):
    # t = import_from_paintings_interval(20, 20)
    populate_database.s().delay()
    # return HttpResponse(t)
    return HttpResponse('let\'s go')
    # return HttpResponse('cc')

def test(request):
    paintings_query = Painting.repository.with_picture().with_readable_name()
    return HttpResponse('yoyoyoyoyoyoyoyoyoyoyo')