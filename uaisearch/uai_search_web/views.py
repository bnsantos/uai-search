from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to uai-search")


def search(request, search_input):
    return HttpResponse("Welcome to uai-search you searched %s" %search_input)