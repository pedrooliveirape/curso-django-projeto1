from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('HOME. Olá Mundo!')


def contato(request):
    return HttpResponse('CONTATO 2')


def sobre(request):
    return HttpResponse('SOBRE 2')
