from django.apps import AppConfig


class BigLibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'big_library'

    def ready(self):
        import big_library.signals

