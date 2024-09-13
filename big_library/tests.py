from django.test import TestCase
from django.urls import reverse

from big_library.models import Article
from big_library.documents import ArticleDocument


class DocumentTestCase(TestCase):

    def setUp(self):
        self.document = Article.objects.create(title="Test Document", description="Test Description",
                                               text="Test Content")

    def test_document_list_view(self):
        response = self.client.get(reverse('big_library:document_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.document.title)

    def test_document_create_view(self):
        response = self.client.post(reverse('big_library:document_create'), {
            'title': 'New Document',
            'rubrics': 'New Rubrics',
            'description': 'New Description',
            'text': 'New Content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Article.objects.filter(title='New Document').exists())

    def test_document_update_view(self):
        response = self.client.post(reverse('big_library:document_update', args=[self.document.id]), {
            'title': 'Updated Document',
            'description': 'Updated Description',
            'text': 'Updated Content'
        })
        self.assertEqual(response.status_code, 302)
        self.document.refresh_from_db()
        self.assertEqual(self.document.title, 'Updated Document')

    def test_document_delete_view(self):
        response = self.client.post(reverse('big_library:document_delete', args=[self.document.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Article.objects.filter(id=self.document.id).exists())


class ElasticsearchSyncTestCase(TestCase):
    def setUp(self):
        self.document = Article.objects.create(
            title="Test Document",
            description="Test Description",
            text="Test Content"
        )

        ArticleDocument().update(self.document)

    def test_document_delete_removes_from_elasticsearch(self):

        es_doc = ArticleDocument.get(id=self.document.id)
        self.assertIsNotNone(es_doc)

        self.document.delete()

        with self.assertRaises(Exception):
            ArticleDocument.get(id=self.document.id)
