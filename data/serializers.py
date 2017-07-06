from rest_framework import serializers

from data.models import Book


class BooklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
