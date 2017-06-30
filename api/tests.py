# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
# Create your tests here.
from django.urls import reverse
from rest_framework import status

from data.models import Books


class ModelTestCase(TestCase):
    def setUp(self):
        self.name = "world class code"
        self.code = Books(name=self.bucketlist_name)

    def test_model_can_create_a_bicketlist(self):
        old_count = Books.objects.count()
        self.bucketlist.save()
        new_count = Books.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_api_can_create_a_buckelist(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucketlist(self):
        booklist = Books.objects.get()
        response = self.client.get(reverse('details'), kwargs={'pk': booklist.id}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, booklist)
