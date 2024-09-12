from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def product_list_view(request: HttpRequest):
    return HttpResponse("<h1>Hello World!</h1>")
