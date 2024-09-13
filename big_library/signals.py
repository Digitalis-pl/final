from django.db.models.signals import post_delete
from django.dispatch import receiver
from big_library.models import Article
from big_library.documents import ArticleDocument


@receiver(post_delete, sender=Article)
def delete_document_from_elasticsearch(sender, instance, **kwargs):

    try:
        document = ArticleDocument.get(id=instance.id)
        document.delete()
    except Exception as e:
        print(f"Ошибка при удалении документа из индекса: {e}")
