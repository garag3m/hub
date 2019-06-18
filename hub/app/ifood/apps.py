from django.apps import AppConfig


class IfoodConfig(AppConfig):
    name = 'app.ifood'

    def ready(self):
        from . import signals
