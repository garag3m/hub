from django.apps import AppConfig


class CereConfig(AppConfig):
    name = 'app.cere'

    def ready(self):
        from . import signals
