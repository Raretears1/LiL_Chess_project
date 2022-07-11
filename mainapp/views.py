from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *


def main_page(request):
    return render(request, 'main.html')


def players_page(request):
    players = Players.objects.all()
    context = {"players": players}
    return render(request, 'players.html', context)


def book_page(request):
    books = Books.objects.all()
    book_count = request.GET.get('count', 3)
    p = Paginator(books, book_count)
    page_number = request.GET.get('page', 1)

    context = {"books": p.page(page_number)}

    return render(request, 'books.html', context)


def debuts_page(request):

    debuts = Debuts.objects.all()

    debut_count = request.GET.get('count', 3)
    p = Paginator(debuts, debut_count)
    page_number = request.GET.get('page', 1)

    openings = Opening.objects.all()

    open_count = request.GET.get('count', 3)
    p1 = Paginator(openings, open_count)
    page_number1 = request.GET.get('page', 1)

    context = {"debuts": debuts, "openings": openings}

    return render(request, 'debuts.html', context)


