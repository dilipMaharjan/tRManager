# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
# Create your views here.
from rest_framework import generics

from api.serializers import BooklistSerializer
from data.models import Book


class CreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BooklistSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BooklistSerializer



def index(request):
    return HttpResponse("Works")
