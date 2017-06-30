# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.template import loader

from data.models import Book, WavFile


def index(request):
    template = loader.get_template('data/index.html')
    data = Book.objects.all()
    context = {'data': data}
    return HttpResponse(template.render(context, request))


def create(request):
    book = Book()
    book.name = request.POST['language']
    book.code = request.POST['code']
    book.save()
    return redirect('/')


def edit(request, id):
    book = Book.objects.get(id=id)
    context = {'book': book}
    return render(request, 'data/edit.html', context)


def update(request, id):
    book = Book.objects.get(id=id)
    book.name = request.POST['language']
    book.code = request.POST['code']
    book.save()
    return redirect('/')


def delete(request, id):
    id = request.GET['id']
    return HttpResponse("The book is" + str(id))


def delete(request, id):
    dog = Book.objects.get(id=id)
    dog.delete()
    return redirect('/')


# gets list of books on the basis of filter provided

def book_by_id(request):
    # list of books based on starting leteer "M"
    # book = Book.objects.filter(name__startswith='M')

    # list of books based on given id
    # book = Book.objects.filter(id=15)

    # list of only 5 matching informations
    # book = Book.objects.all()[:5]

    book = Book.objects.get(Book(name__startswith='J') | Book(code='Ja'))

    for b in book:
        print HttpResponse(b.name)
    return HttpResponse("ok")


def perform_raw_query(request):
    # raw select all query
    book = Book.objects.raw('SELECT * from data_book')

    for b in book:
        print b.name

    

    return HttpResponse("ok")
