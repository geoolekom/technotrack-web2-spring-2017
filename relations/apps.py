from django.apps import AppConfig


class RelationsConfig(AppConfig):
    name = 'relations'

    def ready(self):
        import relations.signals
