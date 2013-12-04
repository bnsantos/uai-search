from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('uai_search_web/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def search(request, search_input):
    return HttpResponse("Welcome to uai-search you searched %s" %search_input)