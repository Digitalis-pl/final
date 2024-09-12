from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from big_library.models import Article


class DocumentTestCase(TestCase):

    def setUp(self):
        self.document = Article.objects.create(title="Test Document", description="Test Description",
                                               content="Test Content")

    def test_document_list_view(self):
        response = self.client.get(reverse('big_library:document_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.document.title)

    def test_document_create_view(self):
        response = self.client.post(reverse('big_library:document_create'), {
            'title': 'New Document',
            'description': 'New Description',
            'content': 'New Content'
        })
        self.assertEqual(response.status_code, 302)  # Redirect to list view
        self.assertTrue(Article.objects.filter(title='New Document').exists())

    def test_document_update_view(self):
        response = self.client.post(reverse('big_library:document_update', args=[self.document.id]), {
            'title': 'Updated Document',
            'description': 'Updated Description',
            'content': 'Updated Content'
        })
        self.assertEqual(response.status_code, 302)
        self.document.refresh_from_db()
        self.assertEqual(self.document.title, 'Updated Document')

    def test_document_delete_view(self):
        response = self.client.post(reverse('big_library:document_delete', args=[self.document.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Article.objects.filter(id=self.document.id).exists())
